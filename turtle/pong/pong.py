import turtle
import pygame  # pygame is used to play sound without stopping
from playsound import playsound  # playsound is used to play sound with a stop


def draw_paddle(paddle, coordinate_x):
    # Draws a rectangular paddle in the middle of the screen on position x
    # Needs to receive a turtle object as the first parameter
    paddle.speed(0)
    paddle.shape("square")
    paddle.color("white")
    paddle.shapesize(stretch_wid=5, stretch_len=1)
    paddle.penup()
    paddle.goto(coordinate_x, 0)


def paddle_1_up():
    y = paddle_1.ycor()
    if y < 220:
        y += 30
    else:
        y = 250
    paddle_1.sety(y)


def paddle_1_down():
    y = paddle_1.ycor()
    if y > -220:
        y += -30
    else:
        y = -250
    paddle_1.sety(y)


def paddle_2_up():
    y = paddle_2.ycor()
    if y < 220:
        y += 30
    else:
        y = 250
    paddle_2.sety(y)


def paddle_2_down():
    y = paddle_2.ycor()
    if y > -220:
        y += -30
    else:
        y = -250
    paddle_2.sety(y)


def reset_ball():
    hud.clear()
    hud.write("{} : {}".format(score_1, score_2), align="center", font=("Press Start 2P", 24, "normal"))
    playsound('258020__kodack__arcade-bleep-sound.mp3')
    ball.goto(0, 0)
    ball.dx *= -1


pygame.init()  # Pygame is used for playing sound effects

# Draws the screen
screen = turtle.Screen()
screen.title("My Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# Initializes and draws  both paddles on screen
paddle_1 = turtle.Turtle()
draw_paddle(paddle_1, -350)

paddle_2 = turtle.Turtle()
draw_paddle(paddle_2, 350)

# Draws ball on center screen
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.08
ball.dy = 0.08

# Initializes score
score_1 = 0
score_2 = 0

# Displays heads-up score
hud = turtle.Turtle()
hud.speed(0)
hud.shape("square")
hud.color("white")
hud.penup()
hud.hideturtle()
hud.goto(0, 260)
hud.write("0 : 0", align="center", font=("Press Start 2P", 24, "normal"))

# keyboard
screen.listen()
screen.onkeypress(paddle_1_up, "w")
screen.onkeypress(paddle_1_down, "s")
screen.onkeypress(paddle_2_up, "Up")
screen.onkeypress(paddle_2_down, "Down")

while True:
    screen.update()

    # ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # collision with the upper wall
    if ball.ycor() > 290:
        pygame.mixer.music.load('bounce.mp3')
        pygame.mixer.music.play()
        ball.sety(290)
        ball.dy *= -1

    # collision with lower wall
    if ball.ycor() < -290:
        pygame.mixer.music.load('bounce.mp3')
        pygame.mixer.music.play()
        ball.sety(-290)
        ball.dy *= -1

    # collision with left wall
    if ball.xcor() < -390:
        score_2 += 1
        reset_ball()

    # collision with right wall
    if ball.xcor() > 390:
        score_1 += 1
        reset_ball()

    # collision with the paddle 1
    if paddle_1.xcor() < ball.xcor() < -330 and paddle_1.ycor() + 50 > ball.ycor() > paddle_1.ycor() - 50:
        pygame.mixer.music.load('bounce.mp3')
        pygame.mixer.music.play()
        ball.setx(-330)
        ball.dx *= -1


    # collision with the paddle 2
    if paddle_2.xcor() > ball.xcor() > 330 and paddle_2.ycor() + 50 > ball.ycor() > paddle_2.ycor() - 50:
        pygame.mixer.music.load('bounce.mp3')
        pygame.mixer.music.play()
        ball.setx(330)
        ball.dx *= -1
