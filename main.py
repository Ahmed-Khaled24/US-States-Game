import pandas as pd
import turtle
from State_Name import Name


# initialize the screen
screen = turtle.Screen()
screen.setup(width=800, height=550)
screen.bgpic("blank_states_img.gif")
screen.title("State guess game")
screen.tracer(0)

# prepare the states data
states_data = pd.read_csv("50_states.csv")
states_data.state = states_data.state.str.lower()


game_on = True
score = 0
while game_on:
    screen.update()
    state_name = Name()

    try:
        user_ans = turtle.textinput(title=f"{score} / 50 Correct.",
                                    prompt="Enter a name of state or [E for exit]: ").lower()
    except:
        # In case the user click cancel in the prompt.
        game_on = False
        break

    if user_ans not in ["e", "E"]:
        ans_pos = states_data[states_data["state"] == user_ans]  # returns a dataframe contains the row
                                                                 # of the user answer if it exists.
        if not ans_pos.empty:
            pos = (ans_pos["x"].item(), ans_pos["y"].item())
            state_name.move_to(pos)
            state_name.type(user_ans.title(), 8)
            score += 1

    else:
        game_on = False


bye = Name()
bye.type("Click on the screen to exit", 20)
screen.exitonclick()
