import smtplib, ssl
import os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "electrogenic14@gmail.com"   
    password = os.getenv("MYPASS")
    print("...............................................................")
    # print(password)
    print("...............................................................")
    
    # password = "wcvhdkrsokfyswom"
    receiver = "electrogenic14@gmail.com"
    my_context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host,port,context=my_context) as server:
        server.login(username,password)
        server.sendmail(username,receiver,message)
 