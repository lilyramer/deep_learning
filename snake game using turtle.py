#Snake game using turtle
import turtle
screen = turtle.Screen()
snake = turtle.Turtle()
snake.color('green')
def forw():
    snake.forward(50)
def backw():
    snake.backward(50)
def turn_right():
    snake.right(45)
def turn_left():
    snake.left(45)

screen.onkey(forw(), 'W')
screen.onkey(backw(), 'S')
screen.onkey(turn_right(), 'A')
screen.onkey(turn_left(), 'D')
screen.listen()

turtle.done()