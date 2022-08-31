import turtle
import pandas

data = pandas.read_csv("./50_states.csv")
screen = turtle.Screen()
texter = turtle.Turtle()
texter.hideturtle()
texter.penup()
image = "./blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
score=0
game_on = True
while game_on:
    answer = screen.textinput(title="guess the state ",
                              prompt="whats another state  q=exit")
    state = data["state"]   #should use data["state"].to_list

    for city in state:
        if city == answer: #shuld use if city in state:
            city_inf = data[data["state"] == answer]
            print(city_inf.x)
            texter.goto(int(city_inf["x"]),int(city_inf.y))
            texter.write(city_inf.state.item()) #answer ~ city_inf.state.item()
            score+=1
    if answer == "q":
        game_on = False
    if score==50:
        texter.goto(-60,0)
        texter.color("green")
        texter.write("You win",font=["Arial",40,"normal"])
        game_on=False
        print()
screen.mainloop()
