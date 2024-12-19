#snake_game_using_turtle
import turtle
screen = turtle.Screen()
turtle.setup(width=200, height=200, startx=100, starty=100)
snake = turtle.Turtle()
turtle.mode(mode ='logo')
snake.color('green')
def forw():
    snake.forward(50)
def backw():
    snake.backward(50)
def turn_right():
    snake.right(30)
def turn_left():
    snake.left(45)
screen.onkey(forw, 'w')
screen.onkey(backw, 's')
screen.onkey(turn_right, 'a')
screen.onkey(turn_left, 'd')
screen.listen()
turtle.done()