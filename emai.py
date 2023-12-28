import smtplib, ssl
host = "smtp.gmail.com"
port = 465

username = "electrogenic14@gmail.com"
password = "wcvhdkrsokfyswom"
receiver = "electrogenic14@gmail.com"
my_context = ssl.create_default_context()
message = """\
Subject: Hiii!
hello from portfolio
"""
with smtplib.SMTP_SSL(host,port,context=my_context) as server:
    server.login(username,password)
    server.sendmail(username,receiver,message)
 