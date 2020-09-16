# Game of pong | . |

# Using the turtle module, and os module(works with os).
import turtle
import os

# Inherit from the Screen class.
wn = turtle.Screen()

# Set Screen Properties
wn.title("Pong version ..::HC::..")
wn.bgcolor("red")
wn.setup(width=1000, height=700)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
# inherit something i need to look up in docs
paddle_a = turtle.Turtle()

# set moving "paddle" properties
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("black")
paddle_a.shapesize(stretch_len=1, stretch_wid=5)
paddle_a.penup()
paddle_a.goto(-400, 0)

# Paddle B
# paddle b object inherit something i need to look up in docs
paddle_b = turtle.Turtle()

# set moving "paddle" properties
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("black")
paddle_b.shapesize(stretch_len=1, stretch_wid=5)
paddle_b.penup()
paddle_b.goto(400, 0)

# Ball
# ball object inherit something i need to look up in docs
ball = turtle.Turtle()

# set moving "ball" properties
ball.speed(0)
ball.shape("square")
ball.color("black")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.08  # moves x 2 pix
ball.dy = 0.08  # moves y 2 pix

# Pen
pen = turtle.Turtle()

pen.speed(0)  # animation speed
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Player A:   Player B:  ", align="center", font=("Courier", 24, "normal"))

# -----------
# Function
# -----------

def PaddleAUp():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def PaddleADown():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def PaddleBUp():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def PaddleBDown():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Keyboard bindings
wn.listen()
wn.onkeypress(PaddleAUp, "w")
wn.onkeypress(PaddleADown, "s")
wn.onkeypress(PaddleBUp, "Up")
wn.onkeypress(PaddleBDown, "Down")

# Main Game loop
while True:  # so ugly <--
    wn.update()

    # ball movement updater
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    # top boarder set
    if ball.ycor() > 340:
        ball.sety(340)
        ball.dy *= -1
        os.system("aplay beeww...wav &")  # "aplay" allows you to play a sound! "beeww...wav" = soundfile.

    # bottom boarder check
    if ball.ycor() < -340:
        ball.sety(-340)
        ball.dy *= -1
        os.system("aplay beeww...wav &")  # "aplay" allows you to play a sound!

    # Right boarder set
    if ball.xcor() > 490:
        ball.setx(0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: " + str(score_a) + " Player B: " + str(score_b), align="center", font=("Courier", 24, "normal"))

    # Left boarder check
    if ball.xcor() < -490:
        ball.setx(0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: " + str(score_a) + " Player B: " + str(score_b), align="center", font=("Courier", 24, "normal"))

    # Ball paddle_b colision
    if (ball.xcor() > 390 and ball.xcor() < 400) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(390)
        ball.dx *= -1
        os.system("aplay beeww...wav &")

    # Ball paddle_a colision
    if (ball.xcor() < -390 and ball.xcor() > -400) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-390)
        ball.dx *= -1
        os.system("aplay beeww...wav &")
