import pandas as pd
import turtle
from State_Name import Name

# initialize the screen
screen = turtle.Screen()
screen.setup(width=800, height=550)
screen.bgpic("blank_states_img.gif")
screen.title("State guess game")
screen.tracer(0)

# prepare the states' data using pandas
states_data = pd.read_csv("50_states.csv")
states_data.state = states_data.state.str.lower()

game_on = True
user_win = False
score = 0
while game_on:
    screen.update()
    state_name = Name()

    try:
        user_ans = turtle.textinput(title=f"{score} / 50 Correct.",
                                    prompt="Enter a name of state or [E for exit]: ").lower()
    except AttributeError:
        # In case the user click cancel in the prompt.
        game_on = False
        break

        # If the user didn't enter e or E for exit.
    if user_ans not in ["e", "E"]:
        ans_pos = states_data[states_data["state"] == user_ans]  # Returns a dataframe contains the row
        # of the user answer if it exists.
        if not ans_pos.empty:
            # Get the coordinates of the state.
            pos = (ans_pos["x"].item(), ans_pos["y"].item())
            state_name.move_to(pos)
            state_name.type(user_ans.title(), 8)
            score += 1

        # If the user answer all the states the game ends
        if score == 50:
            game_on = False
            user_win = True

    else:
        game_on = False

bye = Name()
if not user_win:
    bye.type("Click on the screen to exit", 30)
else:
    bye.type("Congratulations you win", 30)
screen.exitonclick()
