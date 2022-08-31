# iss position  
we are going to learn this teechnology so that we are able to create ISS tracker
so this is the international space station and float high above in the sky and circles earth many many time a day 
![iss](https://raw.githubusercontent.com/wer340/python-angelayu/main/day-33/image/33-iss.png)


-----

### `a`pllication `p`rogramming `i`nterface API
+ api request is kind of similar to going  to bank and trying to get some money out so trying to withdraw some data from their
+ valut 
+ teller bank  can i hep you? what you want ?

we know that it[json] was originally created for `javaScript` but later became almost the `standard of transferring data` across the 
 internet  and reason for it is realy simple  if you take something like a python dictionary lets say you have a a
wardrobe its kind of like you are going to IKEA you spotted a wardrobe you would like but you dont want to carry this home in its 
entirely it might not even fit in your car well what do you do  well in ikea at least the way they have solved it is they sell
you a flat pack  so all the pieces flat against each other and you go home and you build it yourself 
this is equivalent of a `json its very minimalist` it doesnt have a lot of spaces alot of indent 
it just has a couple of symbol to denote which are the key 
once you recevie this json then you can reconstitute it back to your original python dictionary 
#### website check  lng   & lat
[latlong.net](https://www.latlong.net)



---
# module requests
+ `pip install requests`
```python
response = requests.get("http://api.open-notify.org/iss-now.json,parameter")
    response.raise_for_status()  #handle error

```

### response code 
+ 1XX:hold on   // something happening 
+ 2xx:here you go // every thing successful 
+ 3xx:Go away //you  dont actually have permisson 
+ 4xx: you screwed up  // the thing you are looking for doesnt  even exist 
+ 5xx:  i screwed up   // the server that you are making the request to screwed up  maybe server down ,..

#### see check state code [httpstatuses](https://www.httpstatuses.org/)
---
# API use 
+ iss position [open-notify](http://open-notify.org)
+ check sunrise and sunset [sunrise-sunset](https://sunrise-sunset.org/api)
+lat lng  parameter thats required for run api `endpoint?parameter&parameter`

```python
parameter = {"lat": MY_LAT, "lng": MY_LNG, "formatted": 0} # type dict
requests.get("https://api.sunrise-sunset.org/json",parameter)
```
                         
