#snake_game_using_turtle
import turtle
screen = turtle.Screen()
turtle.setup(width=200, height=200, startx=100, starty=100)
snake = turtle.Turtle()
turtle.mode(mode ='logo')
snake.color('green')

def forw():
    snake.setheading(0)
def backw():
    snake.setheading(180)
def turn_right():
    snake.setheading(270)
def turn_left():
    snake.setheading(90)

screen.onkey(forw, 'w')
screen.onkey(backw, 's')
screen.onkey(turn_right, 'a')
screen.onkey(turn_left, 'd')
screen.listen()

def get_cords():
    cords = int(snake.xcor()), int(snake.ycor())
    return cords

position = get_cords()
positions = []

while position not in positions:
    positions.append(position)
    snake.forward(1)
    position = get_cords()

print('you missed')
turtle.done()