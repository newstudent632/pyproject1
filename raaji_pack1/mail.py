import smtplib

sender_mail = "raajiraajus@gmail.com"

rec_email = "kalyansa2001@gmail.com"
password = input(str("place enter your password : ") )
message = "hello mama "

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender_email,password)
print("login success")
server.sensmail(sender_email,rec_email,message)
print("email has sent to",rec_email)
