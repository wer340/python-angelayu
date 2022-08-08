from random import choice
import pandas as pd
import datetime as dt
import smtplib
USER=""
PASSWORD=""

# TODO 1 today date  as tuple
today = dt.datetime.now()
day = today.day
month = today.month
today_tuple = (month, day)

# TODO 2 CSV data to dict as data key
data = pd.read_csv("./birthday_data.csv")
data_dict = {(value.month, value.day): value for (key, value) in
             data.iterrows()}
# print(type(data_dict[(11,22)]))
# print(data_dict[(11,22)])
# breakpoint()
letters = [1, 2, 3]
# TODO 3  select Random letter and replace name
if today_tuple in data_dict:
    number_letter = choice(letters)
    path_letter = "./letter/letter_" + str(number_letter) + ".txt"
    with open(path_letter) as file:
        letter_file = file.read()
        name_person = data_dict[today_tuple]["name"]
        letter_file = letter_file.replace("[Name]",
                                          "❤" + name_person + "❤")
        to_email=data_dict[today_tuple]["email"]
        print(to_email)
        # TODO 4  sent email
        with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
            connection.starttls()
            connection.login(user=USER,password=PASSWORD)
            connection.sendmail(from_addr=USER,to_addrs=to_email,msg=f"subject:Happy birthday{name_person} \n\n {letter_file}")
