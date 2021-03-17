$pastDate = (Get-Date).AddMonths(-1)
$pastDateMonthYear = $pastDate.ToString("MMMM yyyy")
$fileFormatDate = $pastDate.ToString("yyyy-MM")

$User = "eric.watfordweathersociety@gmail.com"
$File = "C:\Users\Alison\Documents\WatfordWeatherSociety\3\EmailPassword.txt"
$cred=New-Object -TypeName System.Management.Automation.PSCredential -ArgumentList $User, (Get-Content $File | ConvertTo-SecureString)
$EmailTo = "alisonealmond@gmail.com,milesbalmond@gmail.com,floranewman5@gmail.com"
$EmailFrom = "eric.watfordweathersociety@gmail.com"
$Subject = "Watford Weather Society - Your $pastDateMonthYear Summary!" 
$Body = "See attached for your monthly weather chart; including rainfall, temperature, and pressure!`n`n`n`nThe Watford Weather Society was set up in May 2020 in memory of Eric Ford. Rest in peace Eric, always in our hearts." 
$filenameAndPath = "C:\Users\Alison\Documents\WatfordWeatherSociety\2\Graphs\$fileFormatDate.pdf"
$SMTPServer = "smtp.gmail.com"
$SMTPMessage = New-Object System.Net.Mail.MailMessage($EmailFrom,$EmailTo,$Subject,$Body)
$attachment = New-Object System.Net.Mail.Attachment($filenameAndPath)
$SMTPMessage.Attachments.Add($attachment)
$SMTPClient = New-Object Net.Mail.SmtpClient($SmtpServer, 587) 
$SMTPClient.EnableSsl = $true 
$SMTPClient.Credentials = New-Object System.Net.NetworkCredential($cred.UserName, $cred.Password); 
$SMTPClient.Send($SMTPMessage)