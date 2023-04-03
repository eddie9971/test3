import random
from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0) # no motion showed no refresh
starting_positions = [(0,0), (-20,0), (-40,0)]
move_distance = 20
up = 90
down = 270
left = 180
right = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in starting_positions:
            self.add_segment(position)

    def add_segment(self,position):
        new_segment = Turtle(shape='square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(move_distance)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def up(self):
        if self.head.heading() != down:
            self.head.setheading(up)

    def down(self):
        if self.head.heading() != up:
            self.head.setheading(down)

    def left(self):
        if self.head.heading() != right:
            self.head.setheading(left)

    def right(self):
        if self.head.heading() != left:
            self.head.setheading(right)


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('blue')
        self.speed(0)
        self.refresh()

    def refresh(self):
        x = random.randint(-280,280)
        y = random.randint(-280, 280)
        self.goto(x,y)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('../snake data.txt') as data:
            self.high_score = int(data.read())
        self.penup()
        self.color('white')
        self.goto(0, 260)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f'Score:{self.score} High Score: {self.high_score}', align='center', font=('Arial',24,'normal'))

    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('../snake data.txt', 'w') as data:
                data.write(f'{self.high_score}')
        self.score = 0
        self.update_score()


    # def game_over(self):
    #     self.goto(0,0)
    #     self.write('GAME OVER!', align='center', font=('Arial',24,'normal'))


if __name__ == '__main__':
    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()
    screen.listen()
    screen.onkey(snake.up,"Up")
    screen.onkey(snake.down,'Down')
    screen.onkey(snake.left,'Left')
    screen.onkey(snake.right,'Right')

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            scoreboard.increase_score()
            snake.extend()

        # Detect collision with wall
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            scoreboard.reset()
            snake.reset()

        # Detect collision with tail
        for segement in snake.segments[1:]:
            if segement == snake.head:
                pass
            elif snake.head.distance(segement) < 10:
                scoreboard.reset()
                snake.reset()
screen.exitonclick()