# The Watford Weather Society

The Watford Weather Society is an automated weather data capture, plot, and email project that I set up in memory of my grandfather Eric.

## Backstory

My grandfather Eric had a true passion for the weather. From around the age of 20 (the same age I was when I created this project), until just a couple months before he passed, he would record the weather every morning from his home in Watford. Yes, you read that right. Every single day without fail he would record the weather. He would do this using his own thermometer (temperature), barometer (pressure), and udometer (rainfall). At the end of each month, he would hand draw a plot of that month's weather.

## Where Do I Come Into This?

Eric always wanted someone to take over this project when he was unable to continue. What I lacked in his commitment to consistent manual weather recording, I had in a decent amount of programming knowledge at the time. So I decided to carry on the project with a modern twist, one that he'd never used himself but had always been fascinated by. I decided to capture, plot, and email the monthly weather report all automatically through code on my computer.

## Capturing the Data

The first step was to find a way to capture the data. I used Python for this part. To do this I used a weather API. I decided on "Weatherbit" which I could use for free and would only have to run my program once a month to gather all the data, looping through each day of the previous month and storing the result in a csv file. Using the coordinates of my grandfather's house, the API would collect data from the nearest weather station on average temperature, minimum temperature, maximum temperature, total rainfall, and average pressure.

## Plotting the Data

To plot the data I used RStudio. I wanted to ensure I matched the plots Eric produced as closely as possible, so I toyed around with different colours and functions in R until I could create the perfect plot in ggplot on his distinctive blue graph paper, with red bars for rainfall, and blue lines for pressure.

## Sending an Email with the Plot

The third of these functions was perhaps the simplest. Using Windows Powershell I just needed to take the plot produced from RStudio, and send an email to anyone on the email list each month with this plot attached.

## Automating This

To automate this, I used Task Scheduler to run functions 1, 2, and 3 in order at the start of each month to collect the data from the previous month, produce the plot, and email this.

## Issues Along the Way / Remarks and Learnings for the Future

The main issue I had with this project is that it required my laptop to be in standby at the right time at the start of each month to run these functions and produce what was needed. I could somewhat get around this by specifying in Task Scheduler that if my laptop was turned off during the time frame in which the functions were meant to run, they could instead run at the next available time that laptop is on. This was fine, but if I were to improve on this project, I would try to run these programs from an external server instead. I would also try and combine this process into one program (probably on Python).

Another issue I encountered is that some weather APIs change their structure in terms of pricing. I originally used a different weather API, but a couple months into using this, I could no longer collect historical data from the month prior without paying a large sum per month, which I unfortunately could not afford. Instead I would have to run the programs everyday to collect the data in this case, rather than just once a month, which would have made it very difficult. So I had to switch APIs from this point onwards, and re-write my code to work with this.

## Final Product

The final product came out exactly as I had desired, and putting his original graphs side-by-side with mine [PICTURES TO BE POSTED HERE], I was really impressed with not only what I'd achieved, but in what it does to honour his memory and commitment to weather records. While I was already quite interested in programming before, this project really kicked off my love for it and my passion for statistics, programming, and data science has grown consistently ever since!
