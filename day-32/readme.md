# Send Email

## use
+  email name and day  of csv   change 
+  set your smtp server  ✅yahoo: smtp.email.yahoo.com   ✅gmail : smtp.gmail.com
+  set user and email 
+  set for email account  less app secure 


# Email
 ### email = name+@+EmailProvider
![smtp](https://raw.githubusercontent.com/wer340/python-angelayu/main/day-32/image/emailwork2.png)

---
## how exactly email work 
this email is going to  move between all of these step and in order to do this it relies on something  called `SMTP`
### `S`imple `M`ail `T`ransfer `P`rotocol
this contain all of the rules that determine how an email is received by mail server passed onto the next
 mail server and how email email can be sent around the internet


---
# TLS
### `t`ransport `l`ayer `s`ecurity 
and it way of securing our connection to all email server
thats way when we are sending an email if somebody else intercepts our email somewhere along the line and they try to read it  
beacuse  this is enaabled that mesasage will be encrypted and it will be impossible for them to read what
is in the content of our email   

---

# python smtp 
python have module smtp  allows send email for any adress

```python 
import smtplib
USER=""
PASSWORD=""
connection=smtplib.SMTP("smtp.mail.yahoo.com")
connection.starttls()
connection.login(user=USER,password=PASSWORD)
connection.sendmail(from_addr=USER,to_addrs="",msg="subject:importAlaram\n\nhello")
connection.close()
```
python have module smtp  allows send email for any adress


----

# less app secure   
+two step pass off❌
+user your phone login off❌
+then  trun on less secure app✅

----
# Gmail
![gmail](https://raw.githubusercontent.com/wer340/python-angelayu/main/day-32/image/aadjust_google_account.png)

# Yahoo
![yahoo](https://raw.githubusercontent.com/wer340/python-angelayu/main/day-32/image/yahomaillessSecure.png)


# for re run program  every day for check day  use  [pythonanywhere](www.pythonanywhere.com)
