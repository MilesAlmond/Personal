library(dplyr)
library(tidyverse)
library(lubridate)
library(ggplot2)
library(gridExtra)
library(cowplot)

prevMonth = Sys.Date() - months(1)
justMonth = format(prevMonth,"%Y-%m")
pdfTitle1 = paste(justMonth,".pdf",sep="")
pdfTitle = paste("USER_PATHXXX/WatfordWeatherSociety/2/Graphs/",pdfTitle1,sep="")
round_any = function(x, accuracy, f=round){f(x/ accuracy) * accuracy}


list.files('USER_PATHXXX/WatfordWeatherSociety/1/Data',full.names=TRUE,pattern=justMonth) %>% lapply(read_csv) %>% bind_rows -> myDF
as.Date(myDF$Date,format = "%d") -> myDF$Date
round((myDF$AveragePressure)*0.029529983071445,2) -> myDF$AveragePressure

monthLength = length(myDF$Date)

minBar = round(min(myDF$AveragePressure),2)
maxBar = round(max(myDF$AveragePressure),2)
avgBar = round(mean(myDF$AveragePressure),1)

totalRainfall = round(sum(myDF$TotalRainfall),2)
rainDays = sum(myDF$TotalRainfall > 0)
wetDays = sum(myDF$TotalRainfall > 0.04)
highestFall = round(max(myDF$TotalRainfall),3)

minTemp = round(min(myDF$MinTemperature),1)
maxTemp = round(max(myDF$MaxTemperature),1)
avgTemp = round(mean(myDF$AverageTemperature),0)

chooseMaxBreaks = max(max(myDF$TotalRainfall),maxTemp/50)

newDF1 = select(myDF,Date,MinTemperature)
as.POSIXct(format(newDF1$Date,"%Y-%m-%d 00:00"),tz = "GMT")  -> newDF1$Date
newDF1 <- rename(newDF1, Temperature = MinTemperature)
newDF2 = select(myDF,Date,MaxTemperature)
as.POSIXct(format(newDF2$Date,"%Y-%m-%d 12:00"),tz = "GMT")  -> newDF2$Date
newDF2 <- rename(newDF2, Temperature = MaxTemperature)
newDF <- bind_rows(newDF1,newDF2)

main <- ggplot() +
  geom_col(myDF,mapping = aes(as.POSIXct(format(Date,"%Y-%m-%d 12:00"),tz="GMT"),TotalRainfall),fill = "indianred2",colour = "dodgerblue3",width=86400) +
  geom_line(newDF,mapping = aes(Date,Temperature/50),colour="dodgerblue3") +
  scale_y_continuous(name = "Rainfall (in)", breaks=seq(0,round_any(chooseMaxBreaks,0.1,f=ceiling)+0.2,by=0.1),sec.axis = sec_axis(~.*50,name = "Temperature (Farenheit)",breaks = seq(round_any(minTemp,10,f=floor)-20,round_any(maxTemp,10,f=ceiling)+20,by=10))) +
  scale_x_datetime(name="Date",date_labels = "%d",date_breaks = "1 day",expand = c(0,0)) +
  theme(axis.text.x = element_text(size = 6.5),axis.text.y = element_text(size = 6,margin=margin(r=2,l=2))) +
  theme(panel.background = element_rect(fill = "white"),panel.grid.major = element_line(colour="skyblue3"),panel.grid.minor = element_line(colour="skyblue"),axis.ticks = element_line(colour="skyblue3"))

top <- ggplot() +
  geom_line(myDF,mapping = aes(as.POSIXct(format(Date,"%Y-%m-%d 12:00"),tz="GMT"),AveragePressure),colour="dodgerblue3") +
  scale_y_continuous(name = "Pressure (in)",breaks=seq(round_any(minBar,0.1,f=floor)-0.2,round_any(maxBar,0.1,f=ceiling)+0.2,by=0.1)) +
  scale_x_datetime(date_labels = "%d",date_breaks = "1 day",expand = c(0,0)) +
  theme(panel.background = element_rect(fill = "white"),panel.grid.major = element_line(colour="skyblue3"),panel.grid.minor = element_line(colour="skyblue"),axis.ticks = element_line(colour="skyblue3")) +
  theme(axis.text.x = element_blank(),axis.title.x = element_blank(),axis.text.y = element_text(size = 6,margin=margin(r=2,l=2)))
  theme(plot.title = element_text(hjust=0.5,colour="dodgerblue3"))

graph <- plot_grid(top, main, ncol = 1,align = 'v', scale = c(monthLength/(monthLength+1),1),rel_heights = c(1,2))

tab1 <- as.data.frame(
  c(
    "Min. Bar" = minBar,
    "Max. Bar" = maxBar,
    "Avg. Bar" = avgBar
  )
)

tab2 <- as.data.frame(
  c(
    "Total Rainfall" = totalRainfall,
    "No. of Rain Days" = rainDays,
    "No. of Wet Days" = wetDays,
    "Highest Fall (24hrs)" = highestFall,
    "Min. Temperature" = minTemp,
    "Max. Temperature" = maxTemp,
    "Avg. Temperature" = avgTemp
  )
)

cols <- matrix("dodgerblue3", nrow(tab1), ncol(tab1))
tt <- ttheme_minimal(core=list(fg_params = list(col = "dodgerblue3"),
                               bg_params = list(col=NA)),
                     rowhead=list(fg_params = list(col="dodgerblue3")),
                     colhead=list(bg_params = list(col=NA)))
p_tab1 <- tableGrob(unname(tab1),theme=tt)

cols <- matrix("dodgerblue3", nrow(tab2), ncol(tab2))
tt <- ttheme_minimal(core=list(fg_params = list(col = "dodgerblue3"),
                               bg_params = list(col=NA)),
                     rowhead=list(fg_params = list(col="dodgerblue3")),
                     colhead=list(bg_params = list(col=NA)))
p_tab2 <- tableGrob(unname(tab2),theme=tt)

info <- plot_grid(p_tab1,p_tab2,nrow=2,rel_heights=c(1,2))
almost <- plot_grid(graph,info, ncol=2, rel_widths = c(3, 1))
title <- ggdraw() + draw_label(format(as.Date(prevMonth),"%B %Y"), fontface='bold',colour="blue")
final <- plot_grid(title, almost, ncol=1, rel_heights=c(0.1, 1))

pdf(pdfTitle,height=8.27,width=11.68)
plot(final)
dev.off()

