import smtplib as sm


def send_mail(message):
    host= "smtp.gmail.com"
    port = 465

    usermail = "amazingsaranya111@gmail.com"
    recipient_mail = "amazingsaranya111@gmail.com"
    password = "keclcdxkdvtmwafd"
    #message = "SMTP check"

    with sm.SMTP_SSL(host,port) as server:
        server.login(usermail,password)
        server.sendmail(usermail,recipient_mail,message)