import time
import turtle
from turtle import Turtle,Screen
from player import Player
from layout import Wall, HorizontalBar, Separator
from ball import Ball
from scoreboard import Scoreboard
from brick import Brick
screen = Screen()
screen.bgcolor('black')
screen.setup(width=800,height=600)
screen.listen()
# screen.tracer(0)

player1=Player()
ball=Ball()
bricks=Brick(800)
bricks.create_brick()
bricks.create_brick()
all_bricks=bricks.all_bricks
for brick in all_bricks:
    print(brick.xcor())
    print(brick.ycor())
    print('--------')


#tworzenie layoutu
wall_left=Wall('left')
wall_right=Wall('right')
bar=HorizontalBar()
separator=Separator()
score_scoreboard=Scoreboard((-200, 230), 'Score')
hearts_scoreboard=Scoreboard((200, 230), 'Hearts')

screen.onkeypress(player1.move_left,'Left')
screen.onkeypress(player1.move_right,'Right')

while hearts_scoreboard.hearts>0:
    # screen.update()
    # time.sleep(ball.move_speed)
    ball.ball_move()
    #uderzanie w sciane
    if ball.xcor()>370 or ball.xcor()<-370:
        ball.ball_bounce_x()
    #przejscie za gracza usuniecie serca
    if ball.ycor()<-320:
        hearts_scoreboard.remove_hearts()
        ball.ball_reset_position()
    # odbijanie sufit
    if ball.ycor()>180:
        ball.ball_bounce_y()
    # odbijanie od gracza
    if ball.distance(player1)<25 and ball.ycor()>-280:
        ball.ball_bounce_y()
    for brick in all_bricks:
        if brick.distance(ball)<30:
            print('pilka uderza')
            ball.ball_bounce_y()
            ball.ball_bounce_x()
            brick.color('red')
            all_bricks.remove(brick)

# zrobic layout ok
# zrobic movement gracza ok
# zrobic scoreboarda ok
# zrobic odbijanie sie od gracza ok
# zrobic odbijanie sie od scian ok
# zrobic klocki ok
# rozmieszcznie klockow
# odbijanie od klockow ok
# zrobic niszczenie blokow ok
#





screen.mainloop()

