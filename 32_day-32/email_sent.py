import smtplib

USER=""
PASSWORD=""


connection=smtplib.SMTP("smtp.mail.yahoo.com")
connection.starttls()
connection.login(user=USER,password=PASSWORD)
connection.sendmail(from_addr=USER,to_addrs="",msg="subject:importAlaram\n\nhello")
connection.close()