# pong game

![pong](https://raw.githubusercontent.com/wer340/python-angelayu/main/day-22/image/pong.png)

# break point this  game    sight me 

![me](https://raw.githubusercontent.com/wer340/python-angelayu/main/day-22/image/my_broken.png)

# original break point 
![origin](https://raw.githubusercontent.com/wer340/python-angelayu/main/day-22/image/breakPoint.png)

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
 ![wall](https://raw.githubusercontent.com/wer340/python-angelayu/main/day-22/image/detect_paddle_des.png)
 
 ## pedal detection
 use distance if was distance betwwen ball and pedaall lesser than 50 then active horizental back
