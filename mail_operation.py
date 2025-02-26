import smtplib as sm
import ssl
import os


def send_mail(message):
    host= "smtp.gmail.com"
    port = 465

    usermail = "amazingsaranya111@gmail.com"
    recipient_mail = "amazingsaranya111@gmail.com"
    #password = "keclcdxkdvtmwafd"
    password = os.getenv("PASSWORD")


    context = ssl.create_default_context()

    with sm.SMTP_SSL(host,port,context = context) as server:
        server.login(usermail,password)
        server.sendmail(usermail,recipient_mail,message)