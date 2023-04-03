import time
from turtle import Screen,Turtle
import random

# for class player
starting_position = (0, -280)
move_distance = 10
finish_line_y = 200

# for class CarManager
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
starting_move_distance = 5
move_increment = 10

# for class Scoreboard
font = ('Calibri', 24, 'normal')


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def go_up(self):
        self.forward(move_distance)

    def go_to_start(self):
        self.goto(starting_position)

    def is_at_finish_line(self):
        if self.ycor() > finish_line_y:
            return True
        else:
            return False


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = starting_move_distance

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle('square')
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(colors))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(starting_move_distance)

    def level_up(self):
        self.car_speed += move_increment


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Level: {self.level}', align='left', font=font)

    def increase_level(self):
        self.level +=1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER!', align='center', font=font)


if __name__ == '__main__':

    screen = Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0)

    player = Player()
    car_manager = CarManager()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(player.go_up, 'Up')
    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        screen.update()

        car_manager.create_car()
        car_manager.move_cars()

        # detect collision with car
        for car in car_manager.all_cars:
            if car.distance(player) < 20:
                game_is_on = False
                scoreboard.game_over()

        # detect successful crossing
        if player.is_at_finish_line():
            player.go_to_start()
            car_manager.level_up()
            scoreboard.increase_level()
    screen.exitonclick()