import datetime as dt
from random import choice
import smtplib

# TODO 1 obtain day of week
now = dt.datetime.now()
weekday = now.weekday()
# print(weekday)
# breakpoint()
# TODO 2 provide quote from txt
with open("quote.txt", encoding="utf-8") as quote:
    list_q = quote.readlines()
    list_q = [item.strip() for item in list_q]
# TODO 3 random choice from quote
qoute_selected = choice(list_q)
# print(qoute_selected)
# breakpoint()
# TODO 4 send mail
USER =""
PASSWORD =""
TO_SEND =""
connection=smtplib.SMTP("smtp.live.com")
connection.starttls()
connection.login(user=USER,password=PASSWORD)
connection.sendmail(from_addr=USER,to_addrs=TO_SEND,msg="subject:importAlaram\n\nhello")
connection.close()
