# pong game
---

### in high order function   callback func  given throuth pranthese term of callback✔  callback()❌
```python
#down() is method from paddle_a instance that given as callback func  without parentheses
screen.onkey(paddle_a.down, "s")
screen.listen()

```

![pong](https://raw.githubusercontent.com/wer340/python-angelayu/main/22_day-22/image/pong.png)

# break point this  game    sight me 

![me](https://raw.githubusercontent.com/wer340/python-angelayu/main/22_day-22/image/my_broken.png)

# original break point 
![origin](https://raw.githubusercontent.com/wer340/python-angelayu/main/22_day-22/image/breakPoint.png)

-----

# important issue

## diagnoal move 

```python 
 def move(self):  # diagonal move  y=x
        x_new = self.xcor() + self.x_move
        y_new = self.ycor() + self.y_move
        self.goto(x_new, y_new)
```

## vertical and horizental back 

ball after reach to wall back from side   

```python
def bounce_y(self):
        self.y_move *= -1

def bounce_x(self):
        self.x_move *= -1
 ```
 ![wall](https://raw.githubusercontent.com/wer340/python-angelayu/main/22_day-22/image/detect_paddle_des.png)
 
 ## pedal detection
 use distance if was distance betwwen ball and pedaall lesser than 50 then active horizental back
 
 ## scoreboard issue 
notice self.goto pre define self.write() method

```python
class Scoeboaard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(-40, 250)  #✔1️⃣ notice goto pre define write method
        self.write(f"b :{self.b_score} a :{self.a_score} ",align=ALIGN, font=FONT)#✔2️⃣
 ```       
