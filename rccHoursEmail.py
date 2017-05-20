#!/usr/bin/python

import smtplib
from email.mime.text import MIMEText

body = "#task\n#priority High\n"
body += "Hello, this is a reminder to please fill in your RCC hours for the week.\n"
body += "\nWe recommend filling in any hours that were not captured by your other tickets here. You can use the Category Personal Computing -> Networking -> WiFi for general hours helping students.\n"
body += "\nIf you have other hours to record, such as Cluster Maintenence, we recommend you create a new ticket and log the hours there.\n"
body += "\nThank you!"

def sendEmail(address):
    # Change to your own account information
    to = 'support@acomp.stanford.edu'
    gmail_user = 'stanfordrccbot@gmail.com'
    gmail_password = 'l3tRCCB0t1n'
    smtpserver = smtplib.SMTP('smtp.gmail.com', 587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(gmail_user, gmail_password)

    msg = MIMEText("#assignee " + address + "\n" + body) # assign the rcc here
    msg['Subject'] = 'Please update your RCC hours'
    msg['From'] = gmail_user
    msg['To'] = to
    smtpserver.sendmail(gmail_user, [to], msg.as_string())
    smtpserver.quit()


body = "#task\n#priority High\n"
body += "Hello, this is a reminder to please fill in your RCC hours for the week.\n"
body += "\nWe recommend filling in any hours that were not captured by your other tickets here. You can use the Category Personal Computing -> Networking -> WiFi for general hours helping students.\n"
body += "\nIf you have other hours to record, such as Cluster Maintenence, we recommend you create a new ticket and log the hours there.\n"
body += "\nThank you!"

rccs = ["kelsey17@stanford.edu","chengyue@stanford.edu","ishans@stanford.edu","mushittu@stanford.edu","sanchezn@stanford.edu","byahya@stanford.edu","mengler@stanford.edu","bhiggins@stanford.edu","saman1@stanford.edu","akhaledi@stanford.edu","pperozo@stanford.edu","samsunde@stanford.edu","rmgrab@stanford.edu","jakerach@stanford.edu","eliza2@stanford.edu","eholmvik@stanford.edu","yushi@stanford.edu","trzhao@stanford.edu","helennn@stanford.edu","j3nidad@stanford.edu","theha@stanford.edu","angiec96@stanford.edu","sandips@stanford.edu","yasminb@stanford.edu","kkanagal@stanford.edu","jbelz@stanford.edu","jli439@stanford.edu","chung888@stanford.edu","tmarkov@stanford.edu","jevans2@stanford.edu","bsheffer@stanford.edu","caraha@stanford.edu","mdu96@stanford.edu","debnil@stanford.edu","alexgill@stanford.edu","reganp@stanford.edu","cqyuan@stanford.edu","jcingel@stanford.edu","devangi@stanford.edu","sklovett@stanford.edu","iprado@stanford.edu","isathomp@stanford.edu","mmahlock@stanford.edu","anniehu@stanford.edu","ahardy@stanford.edu","oakerele@stanford.edu","addisonl@stanford.edu","cwads@stanford.edu","cheson@stanford.edu","thua@stanford.edu","amulia@stanford.edu","minhan@stanford.edu","younes@stanford.edu","arjunvb@stanford.edu","elenamb@stanford.edu","ebauer13@stanford.edu","hernandz@stanford.edu","chenyaoy@stanford.edu","miland@stanford.edu","adas17@stanford.edu","jhmleung@stanford.edu","hugov65@stanford.edu","jkipyato@stanford.edu","madelynb@stanford.edu","bthomson@stanford.edu","hcshen@stanford.edu","liujas00@stanford.edu","eseraiah@stanford.edu","avina322@stanford.edu","rmu@stanford.edu","eawotwi@stanford.edu","samhinsh@stanford.edu","dhau@stanford.edu","abielg@stanford.edu","gla@stanford.edu","jcbuena@stanford.edu","tvjensen@stanford.edu","schopra8@stanford.edu","thomklau@stanford.edu","lucianos@stanford.edu","katys@stanford.edu","nhall2@stanford.edu","nikmart@stanford.edu","mefazio@stanford.edu","bklopfer@stanford.edu","jianlijl@stanford.edu","sanggook@stanford.edu","schub@stanford.edu","liorbu@stanford.edu","troccoli@stanford.edu","slindsay@stanford.edu","xywang@stanford.edu","jordanm1@stanford.edu","mchenja@stanford.edu"]

for rcc in rccs:
    sendEmail(rcc)
