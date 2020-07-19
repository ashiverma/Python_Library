import smtplib

From = input("From: ")
Password = input("Type your account Password and hit enter: ")
To = input("Type the receipent email address and hit enter: ")
Subject = input("Type the Subject and hit enter: ")
Message_Body = input("Type the message you want to send and hit enter: ")

# Prepare the actual message
msg = """From: %s\n To: %s\nSubject: %s\n\n%s
    """ % (From, ", ".join(To), Subject, Message_Body)

while True:
    try:
        line = input()
    except EOFError:
        break
    if not line:
        break
    msg = msg + line

server = smtplib.SMTP("smtp.gmail.com", 587)   # 587 = port number
server.ehlo() # check the smtp connection
server.starttls() # Secure and Start the connection
server.login(From, Password)
server.sendmail(From, To, msg)
server.close()
print("Cheers, Your email has been sent :)")