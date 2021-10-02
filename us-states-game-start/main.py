import turtle
import pandas
screen = turtle.Screen()
screen.title("US-States-Game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_data = pandas.read_csv("50_states.csv")
states_list = states_data.state.to_list()
guess_states = []

while len(guess_states) < 60:

    u_s = screen.textinput(title =f"{len(guess_states)}/50 States selceted",prompt = "Whats the state name ")
    user_answer = u_s.title()
    if user_answer == "Exit":
        miised_states=[state for state in states_list if state not in guess_states]
        # miised_states = []
        # for states in states_list:
        #     if states not in guess_states:
        #         miised_states.append(states)
        new_data = pandas.DataFrame(miised_states)
        new_data.to_csv("i need.csv")
        print(miised_states)
        break
    if user_answer in states_list:
        guess_states.append(user_answer)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        s_d = states_data[states_data.state == user_answer]
        t.goto(int(s_d.x),int(s_d.y))
        t.write(user_answer)


# screen.exitonclick()
