import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.tracer(0)

states_data = pd.read_csv("50_states.csv")
# print(states_data)

answer_state = ""

# print(states_data.x[states_data.state == answer_state])

def show_states():
    tm = turtle.Turtle()
    turtle_x = states_data.x[states_data.state == answer_state].item()
    turtle_y = states_data.y[states_data.state == answer_state].item()
    # print(f"{turtle_x} is x \n {turtle_y} is y")
    tm.penup()
    tm.color("black")
    tm.goto(turtle_x,turtle_y)
    tm.write(arg=answer_state,move=False,align="center",font=("Arial",8,"normal"))

# print_states()
score = 0
guessed_states = []

while len(guessed_states)<50:
    answer_state = screen.textinput(title=f"{score}/50 States correct!", prompt="Make a guess!").title()
    if answer_state == "Exit":
        break
    if answer_state in list(states_data.state) and answer_state not in guessed_states:
        show_states()
        score += 1
        guessed_states.append(answer_state)

#generate a csv file containing all the missing states
# non_guessed_states_dict = {
#     "states_list" : [],
#     "x_cor": [],
#     "y_cor": []
# }
# for state in states_data.state.to_list():
#     if state not in guessed_states:
#         non_guessed_states_dict["states_list"].append(state)
#         non_guessed_states_dict["x_cor"].append(states_data.x[states_data.state == state].item())
#         non_guessed_states_dict["y_cor"].append(states_data.y[states_data.state == state].item())

non_guessed_states = [
    [states,
    states_data.x[states_data.state == states].item(),
    states_data.y[states_data.state == states].item()]
    for states in states_data.state.to_list() if states not in guessed_states
]
# print(non_guessed_states)
# non_guessed_states_dict = {"states_list":[s for s,_,_ in non_guessed_states],
#                            "x_cor":[x for _,x,_ in non_guessed_states],
#                            "y_cor":[y for _,_,y in non_guessed_states]}
# print(non_guessed_states_dict)
# print(non_guessed_states_dict)



leftover = pd.DataFrame(non_guessed_states,columns=["states","x_cor","y_cor"])
leftover.to_csv("revise_states.csv",index=False)

