import smtplib
import email.message
import requests
import time


def send_gmail(gmail_user, gmail_pass, sent_from, sent_to, email_text):
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(gmail_user, gmail_pass)
        server.ehlo()
        server.sendmail(sent_from, sent_to, email_text)
        server.close()

        print ('Email sent!')
    except:
        print ('Something went wrong...')


def blockWatch(delegate, auth, missed):
    if missed < requests.get(get_delegate, auth=authAPI,params=delegate).json()['result']['turnsMissed']:
        missed = requests.get(get_delegate, auth=authAPI,params=delegate).json()['result']['turnsMissed']
        message = "Delegate %s has missed a new block! \n Current lost blocks: %s" % (delegate['address'],missed)
        m.set_payload(message)
        email_text = m.as_string()
        send_gmail(gmail_user, gmail_pass, sent_from, sent_to, email_text)
        return missed
    else:
        print("No missed blocks for Delegate: %s" % delegate['address'])
        return missed


gmail_user = 'gmailuser@gmail.com'
gmail_pass = 'gmailpassword'

sent_from = gmail_user
sent_to = gmail_user

m = email.message.Message()
m['From'] = gmail_user
m['To'] = gmail_user
m['Subject'] = "Missed Block!!"


site = 'http://127.0.0.1:5171'
get_delegate = site + '/get_delegate'
API_username = 'apiUser'
API_password = 'apiPass'

authAPI = requests.auth.HTTPBasicAuth(API_username,API_password)
response = requests.get(site, auth=authAPI)

delegate1 = {"address", "0x9bb94ead4eeb66135e118babba87b424657afe9d"}
delegate2 = {"address", "0x23a52d17377e7f69c279a094f90603244a4eb781"}

missed = 0
missed2 = 0

if __name__ == "__main__":
    while True:
        missed = blockWatch(delegate1, authAPI, missed)
        missed2 = blockWatch(delegate2, authAPI, missed2)
        time.sleep(30)
