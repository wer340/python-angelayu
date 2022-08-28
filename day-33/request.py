import requests

response=requests.get("http://api.open-notify.org/iss-now.json")
if response.status_code==404:
    raise Exception("this request is not exist")
elif response.status_code==401:
    raise Exception("You not Authorized for this request ")