from turtle import Turtle,Screen
import time
from snake_class import Snake
from food import Food
from score_snake import Score


screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake=Snake()
food=Food()
score_board=Score()

screen.listen()
#use arrow keys or asdw keys for movements
screen.onkey(snake.forward,"Right") or screen.onkey(snake.forward,"d") 
screen.onkey(snake.upward,"Up") or screen.onkey(snake.upward,"w")
screen.onkey(snake.downward,"Down") or screen.onkey(snake.downward,"s")
screen.onkey(snake.left,"Left") or screen.onkey(snake.left,"a")


game_is_on=True

while game_is_on:
    screen.update()
    time.sleep(0.1) 
    snake.move()

    #detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_board.inc_score()
        
    #detect collision with wall
    if snake.head.xcor()>290 or snake.head.xcor() < (-290) or snake.head.ycor() > 280 or snake.head.ycor() < (-280):
        score_board.reset()
        snake.reset()
    
    #detect collision with tail
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            score_board.reset()
            snake.reset()

screen.exitonclick()

