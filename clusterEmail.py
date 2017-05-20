#!/usr/bin/python

import smtplib
from email.mime.text import MIMEText

clusters = ["rains5-cm@rescomp.stanford.edu", "rains31-cm@rescomp.stanford.edu", "ev54-cm@rescomp.stanford.edu", "ev-c-rcc@rescomp.stanford.edu", "ev-b-rcc@rescomp.stanford.edu", "ev-a-cm@rescomp.stanford.edu", "lyman-cm@rescomp.stanford.edu", "rains-y-rcc@rescomp.stanford.edu", "munger-t-rcc@rescomp.stanford.edu", "munger5-cm@rescomp.stanford.edu", "mirrielees-cm@rescomp.stanford.edu", "suites-cm@rescomp.stanford.edu", "ev-m-cm@rescomp.stanford.edu", "ev-l-rcc@rescomp.stanford.edu", "ev-k-rcc@rescomp.stanford.edu", "blkw-cm@rescomp.stanford.edu", "evst5-cm@rescomp.stanford.edu", "st5-cm@rescomp.stanford.edu", "ev-h-rcc@rescomp.stanford.edu", "hulme-cm@rescomp.stanford.edu", "ev-f-rcc@rescomp.stanford.edu", "ev-e-rcc@rescomp.stanford.edu", "naranja-cm@rescomp.stanford.edu", "lag-east-cm@rescomp.stanford.edu", "lag-west-cm@rescomp.stanford.edu", "robinson-cm@rescomp.stanford.edu", "potter-cm@rescomp.stanford.edu", "schiff-cm@rescomp.stanford.edu", "frosoco-cm@rescomp.stanford.edu", "yost-cm@rescomp.stanford.edu", "murray-cm@rescomp.stanford.edu", "east-cm@rescomp.stanford.edu", "flomo-west-cm@rescomp.stanford.edu", "flomo-east-cm@rescomp.stanford.edu", "cromem-cm@rescomp.stanford.edu", "crothers-cm@rescomp.stanford.edu", "branner-cm@rescomp.stanford.edu", "cedro-cm@rescomp.stanford.edu", "arroyo-cm@rescomp.stanford.edu", "toyon-cm@rescomp.stanford.edu", "zapata-cm@rescomp.stanford.edu", "burbank-cm@rescomp.stanford.edu", "serra-cm@rescomp.stanford.edu", "larkin-cm@rescomp.stanford.edu", "donner-cm@rescomp.stanford.edu", "roble-cm@rescomp.stanford.edu", "lantana-cm@rescomp.stanford.edu", "kimball-cm@rescomp.stanford.edu", "ujamaa-cm@rescomp.stanford.edu", "narnia-cm@rescomp.stanford.edu", "muwekma-cm@rescomp.stanford.edu", "hausmit-cm@rescomp.stanford.edu", "mars-cm@rescomp.stanford.edu", "kappasig-cm@rescomp.stanford.edu", "ka-cm@rescomp.stanford.edu", "kairos-cm@rescomp.stanford.edu", "jerry-cm@rescomp.stanford.edu", "italiana-cm@rescomp.stanford.edu", "hammarskjold-cm@rescomp.stanford.edu", "grove-cm@rescomp.stanford.edu", "french-cm@rescomp.stanford.edu", "ebf-cm@rescomp.stanford.edu", "durand-cm@rescomp.stanford.edu", "tridelt-cm@rescomp.stanford.edu", "chithetachi-cm@rescomp.stanford.edu", "columbae-cm@rescomp.stanford.edu", "bob-cm@rescomp.stanford.edu", "dlrs717-cm@rescomp.stanford.edu", "lmta680-cm@rescomp.stanford.edu", "trancos-cm@rescomp.stanford.edu", "humanities-cm@rescomp.stanford.edu", "soto-cm@rescomp.stanford.edu", "rinconada-cm@rescomp.stanford.edu", "otero-cm@rescomp.stanford.edu", "okada-cm@rescomp.stanford.edu", "junipero-cm@rescomp.stanford.edu", "zap-cm@rescomp.stanford.edu", "xanadu-cm@rescomp.stanford.edu", "theta-cm@rescomp.stanford.edu", "thetadelt-cm@rescomp.stanford.edu", "terra-cm@rescomp.stanford.edu", "synergy-cm@rescomp.stanford.edu", "storey-cm@rescomp.stanford.edu", "slavdom-cm@rescomp.stanford.edu", "sigmanu-cm@rescomp.stanford.edu", "sae-cm@rescomp.stanford.edu", "roth-cm@rescomp.stanford.edu", "piphi-cm@rescomp.stanford.edu", "phisig-cm@rescomp.stanford.edu", "phipsi-cm@rescomp.stanford.edu", "schwab-rcc@rescomp.stanford.edu", "quil-cm@rescomp.stanford.edu"]

body = "#task\n#priority High\n"
body += "Hello, this is a reminder to please fill in your RCC hours for the week. We recommend filling in any hours that were not captured by your other tickets here. You can use the Category Personal Computing -> Networking -> WiFi for general hours helping students.\n"
body += "\nIf you have other hours to record, such as Cluster Maintenence, we recommend you create a new ticket and log the hours there.\n"
body += "\nThank you"

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

    msg = MIMEText("#assignee " + address + "\n" + body) # assign the cluster here
    msg['Subject'] = 'Please check on your cluster'
    msg['From'] = gmail_user
    msg['To'] = to
    smtpserver.sendmail(gmail_user, [to], msg.as_string())
    smtpserver.quit()

for cluster in clusters:
    #print(cluster)
    sendMail(cluster)
