import requests
from datetime import datetime
import time
import smtplib
# email data fill
USER=""
PASSWORD=""
MY_EMAIL=""
# coordinate your location
MY_LNG = 51.388973
MY_LAT = 35.689198


def iss_pos():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    lng = float(data["iss_position"]["longitude"])
    lat = float(data["iss_position"]["latitude"])
    iss_position = (lng, lat)
    if MY_LAT - 5 <= lat <= MY_LAT + 5 and MY_LNG - 5 <= lng <= MY_LNG + 5:
        return True


def is_sunset():
    parameter = {"lat": MY_LAT, "lng": MY_LNG, "formatted": 0}
    state = requests.get("https://api.sunrise-sunset.org/json",
                         parameter)
    sunrise = int(
        state.json()["results"]["sunrise"].split("T")[1].split(":")[
            0])
    sunset = int(
        state.json()["results"]["sunset"].split("T")[1].split(":")[0])
    hour_now = datetime.now().hour
    if hour_now > sunset or hour_now < sunrise:
        return True

while True:
    time.sleep(60)

    if iss_pos() and is_sunset():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=USER, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL,
                            msg="subject:ISS Notification\n\nhello mr name Iss in sky there is above you")
        connection.close()
