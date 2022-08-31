import turtle

screen = turtle.Screen()
image = "./blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


def get_cordinate(x, y):
    print(x, y)


turtle.onscreenclick(get_cordinate)

screen.mainloop()
# screen.exitonclick()
# use mainloop replace mailnloop in order to  after click windows not close