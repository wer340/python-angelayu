import requests
from datetime import datetime
MY_LNG=51.388973
MY_LAT=35.689198
response=requests.get("http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data=response.json()
long=float(data["iss_position"]["longitude"])
lat=float(data["iss_position"]["latitude"])
iss_position=(long,lat)

parameter={
    "lat":MY_LAT,
    "lng":MY_LNG,
    "formatted" :0
}

sunTime=requests.get("https://api.sunrise-sunset.org/json",parameter)
sunrise=int(sunTime.json()["results"]["sunrise"].split("T")[1].split(":")[0])
sunrise=int(sunTime.json()["results"]["sunset"].split("T")[1].split(":")[0])
time_now=datetime.now()

