import random
import time

class Game:
    def __init__(self):
        self.snake = [(225, 225), (210, 225), (195, 225)]
        self.food = self.generate_food()
        self.bomb = None
        self.bomb_time = 0
        self.direction = (15, 0)
        self.is_game_over = False
        self.is_running = False
        self.score = 0
        self.food_counter = 0

    def start_game(self):
        # Reset alla the parameters before restart a new game session
        self.snake = [(225, 225), (210, 225), (195, 225)]
        self.food = self.generate_food()
        self.bomb = None
        self.bomb_time = 0
        self.direction = (15, 0)
        self.is_running = True
        self.is_game_over = False
        self.score = 0
        self.food_counter = 0
        
    # new randomic position for the apple (ALIGNED WITH THE GRID!)
    def generate_food(self):
        while True:
            x = random.randint(0, (900 // 15) - 1) * 15
            y = random.randint(60 // 15, (600 // 15) - 1) * 15
            if (x, y) not in self.snake:
                return (x, y)

    def update(self):
        if self.is_running:
            self.move_snake()
            self.check_collisions()
            self.check_bomb_time()
        pass

    # manage the position of the snake 
    def move_snake(self):
        # position of the head
        new_head = (self.snake[0][0] + self.direction[0], self.snake[0][1] + self.direction[1])
        # add the new head and remove the last part of the body
        self.snake = [new_head] + self.snake

        if new_head == self.food:
            # if the snake eats the apple
            self.score += 1
            self.food_counter += 1
            self.food = self.generate_food()
            # Ogni 3/4 apples a new bomb is printed
            if self.food_counter % random.randint(3, 4) == 0 and not self.bomb:
                self.spawn_bomb()
        elif self.bomb and new_head == self.bomb:
            # if the snake hits the bomb: game over
            self.is_running = False
            self.is_game_over = True
        else:
            # otherwise remove the queue (movement)
            self.snake.pop()

    def change_direction(self, dx, dy):
        # manage the change direction (NB: cannot change direction of 180 degrees!!)
        if (dx, dy) != (-self.direction[0], -self.direction[1]):
            self.direction = (dx, dy)

    # manage the collisions with the pitch or with himself
    def check_collisions(self):
        head = self.snake[0]
        if (
            head[0] < 0 or head[0] >= 900 or
            head[1] < 60 or head[1] >= 600 or
            head in self.snake[1:]
        ):
            self.is_running = False
            self.is_game_over = True

    def check_bomb_time(self):
        # delete the bomb after 10 seconds
        if self.bomb and time.time() - self.bomb_time >= 10:
            self.bomb = None

    def spawn_bomb(self):
        # position of the bomb (free but not over the snake)
        while True:
            bomb_pos = self.generate_food()
            if bomb_pos != self.food and bomb_pos not in self.snake:
                self.bomb = bomb_pos
                self.bomb_time = time.time()
                break