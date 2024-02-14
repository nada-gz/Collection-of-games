import turtle

# Creating main screen
def main_screen():
    global menuscreen
    menuscreen = turtle.Screen()
    menuscreen.title("Pong Main Menu")
    menuscreen.bgcolor("black")
    menuscreen.tracer(0)


main_screen()

# Create Pen
pen = turtle.Turtle()
pen.hideturtle()
pen.pencolor("black")
pen.fillcolor("white")

SButton_x = -50
SButton_y = 100
SButton_length = 130
SButton_width = 50

HButton_x = -50
HButton_y = 0
HButton_length = 130
HButton_width = 50

TButton_x = -50
TButton_y = -100
TButton_length = 130
TButton_width = 50

Back_Button_x = -200
Back_Button_y = -300
Back_Button_length = 130
Back_Button_width = 50

# creating Start button
def draw_sbutton(pen, message="Start Game"):
    pen.penup()
    pen.begin_fill()
    pen.goto(SButton_x, SButton_y)
    pen.goto(SButton_x + SButton_length, SButton_y)
    pen.goto(SButton_x + SButton_length, SButton_y + SButton_width)
    pen.goto(SButton_x, SButton_y + SButton_width)
    pen.goto(SButton_x, SButton_y)
    pen.end_fill()
    pen.goto(SButton_x + 15, SButton_y + 15)
    pen.goto(SButton_x + 15, SButton_y + 15)
    pen.write(message, font=("Arial", 15, "normal"))

# Creating Rules button
def draw_hbutton(pen, message="    Rules"):
    pen.penup()
    pen.begin_fill()
    pen.goto(HButton_x, HButton_y)
    pen.goto(HButton_x + HButton_length, HButton_y)
    pen.goto(HButton_x + HButton_length, HButton_y + HButton_width)
    pen.goto(HButton_x, HButton_y + HButton_width)
    pen.goto(HButton_x, HButton_y)
    pen.end_fill()
    pen.goto(HButton_x + 15, HButton_y + 15)
    pen.goto(HButton_x + 15, HButton_y + 15)
    pen.write(message, font=("Arial", 15, "normal"))

# creating Tutorial button
def draw_tbutton(pen, message="  Tutorial"):
    pen.penup()
    pen.begin_fill()
    pen.goto(TButton_x, TButton_y)
    pen.goto(TButton_x + TButton_length, TButton_y)
    pen.goto(TButton_x + TButton_length, TButton_y + TButton_width)
    pen.goto(TButton_x, TButton_y + TButton_width)
    pen.goto(TButton_x, TButton_y)
    pen.end_fill()
    pen.goto(TButton_x + 15, TButton_y + 15)
    pen.goto(TButton_x + 15, TButton_y + 15)
    pen.write(message, font=("Arial", 15, "normal"))


# creating a back button
def draw_back_button(pen, message="Back"):
    pen.penup()
    pen.begin_fill()
    pen.goto(Back_Button_x, Back_Button_y)
    pen.goto(Back_Button_x + Back_Button_length, Back_Button_y)
    pen.goto(Back_Button_x + Back_Button_length, Back_Button_y + Back_Button_width)
    pen.goto(Back_Button_x, Back_Button_y + Back_Button_width)
    pen.goto(Back_Button_x, Back_Button_y)
    pen.end_fill()
    pen.goto(Back_Button_x + 15, Back_Button_y + 15)
    pen.goto(Back_Button_x + 15, Back_Button_y + 15)
    pen.write(message, font=("Arial", 15, "normal"))

# Clicking on back button
def back_button_click(x, y):
    if Back_Button_x <= x <= (Back_Button_x + Back_Button_length):
        if Back_Button_y <= y <= (Back_Button_y + Back_Button_width):
            print("back")
            menuscreen.clearscreen()
            main_screen()
            draw_sbutton(pen)
            draw_hbutton(pen)
            draw_tbutton(pen)
            menuscreen.onclick(button_click)

# Clicking on Button
def button_click(x, y):
    if HButton_x <= x <= (SButton_x + SButton_length):
        if SButton_y <= y <= (SButton_y + SButton_width):
            print('Start Game')
            menuscreen.clearscreen()

            wn = turtle.Screen()
            wn.title("Pong")
            wn.bgcolor("black")
            wn.setup(width=800, height=600)
            # tracer = stops window from updating
            wn.tracer(0)

            # Score
            score_a = 0
            score_b = 0

            # Pen
            pen = turtle.Turtle()
            pen.speed(0)
            pen.color("white")
            pen.penup()
            pen.hideturtle()
            pen.goto(0, 260)
            pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "normal"))

            # Paddle A
            paddle_a = turtle.Turtle()
            paddle_a.speed(0)
            paddle_a.shape("square")
            paddle_a.color("white")
            paddle_a.shapesize(stretch_wid=5, stretch_len=1)
            paddle_a.penup()
            paddle_a.goto(-350, 0)

            # Paddle B
            paddle_b = turtle.Turtle()
            paddle_b.speed(0)
            paddle_b.shape("square")
            paddle_b.color("white")
            paddle_b.shapesize(stretch_wid=5, stretch_len=1)
            paddle_b.penup()
            paddle_b.goto(350, 0)

            # Ball
            ball = turtle.Turtle()
            ball.speed(0)
            ball.shape("square")
            ball.color("white")
            ball.penup()
            ball.goto(0, 0)
            ball.dx = 0.15
            ball.dy = -0.15

            # Function to move paddle a up
            def paddle_a_up():
                y = paddle_a.ycor()
                y += 20
                paddle_a.sety(y)

            # Function to move paddle a down
            def paddle_a_down():
                y = paddle_a.ycor()
                y -= 20
                paddle_a.sety(y)

            # Function to move paddle b up
            def paddle_b_up():
                y = paddle_b.ycor()
                y += 20
                paddle_b.sety(y)

            # Function to move paddle b down
            def paddle_b_down():
                y = paddle_b.ycor()
                y -= 20
                paddle_b.sety(y)

            wn.listen()
            wn.onkeypress(paddle_a_up, "w")
            wn.onkeypress(paddle_a_down, "s")
            wn.onkeypress(paddle_b_up, "Up")
            wn.onkeypress(paddle_b_down, "Down")

            # Main game loop
            while True:
                wn.update()
                #    move ball
                ball.setx(ball.xcor() + ball.dx)
                ball.sety(ball.ycor() + ball.dy)

                # border checking
                if ball.ycor() > 290:
                    ball.sety(290)
                    ball.dy *= -1

                if ball.ycor() < -290:
                    ball.sety(-290)
                    ball.dy *= -1

                if ball.xcor() > 390:
                    ball.goto(0, 0)
                    ball.dx *= -1
                    score_a += 1
                    pen.clear()
                    pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center",
                              font=("Courier", 24, "normal"))

                if ball.xcor() < -390:
                    ball.goto(0, 0)
                    ball.dx *= -1
                    score_b += 1
                    pen.clear()
                    pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center",
                              font=("Courier", 24, "normal"))

                # paddle and ball collisions
                if 340 < ball.xcor() < 350 and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
                    ball.setx(340)
                    ball.dx *= -1

                if -340 > ball.xcor() > -350 and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
                    ball.setx(-340)
                    ball.dx *= -1

                if score_a > 9:
                    pen.clear()
                    pen.write("GAME END! Player A wins!", align="center", font=("Courier", 24, "normal"))
                    ball.dx = 0
                    ball.dy = 0

                elif score_b > 9:
                    pen.clear()
                    pen.write("GAME END! Player B wins!", align="center", font=("Courier", 24, "normal"))
                    ball.dx = 0
                    ball.dy = 0

    if HButton_x <= x <= (HButton_x + HButton_length):
        if HButton_y <= y <= (HButton_y + HButton_width):
            print("clicked")
            menuscreen.clearscreen()
            menuscreen.bgcolor("black")
            pen = turtle.Turtle()
            pen.hideturtle()
            pen.pencolor("white")
            pen.write("Score 10 points first to win", align="center", font=("Courier", 24, "normal"))
            draw_back_button(pen)
            menuscreen.onclick(back_button_click)

    if TButton_x <= x <= (TButton_x + TButton_length):
        if TButton_y <= y <= (TButton_y + TButton_width):
            print("clicked")
            menuscreen.clearscreen()
            menuscreen.bgcolor("black")
            pen = turtle.Turtle()
            pen.hideturtle()
            pen.pencolor("white")
            pen.write("Player A uses w key to go up and s to go down. \n Player B uses up and down arrow keys.", align="center", font=("Courier", 24, "normal"))
            draw_back_button(pen)
            menuscreen.onclick(back_button_click)


menuscreen.onclick(button_click)


draw_sbutton(pen)
draw_hbutton(pen)
draw_tbutton(pen)
turtle.done()
# ^^wait for user to close screen
