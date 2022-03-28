from turtle import Turtle


class Name (Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def move_to(self, state_position):
        self.goto(state_position)

    def type(self, state_name, fontSize):
        self.write(arg=state_name, align="center", font=('Candara', fontSize, 'normal'))

