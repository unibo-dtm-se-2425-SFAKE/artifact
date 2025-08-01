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

    def generate_food(self):
        # new randomic position for the apple (ALIGNED WITH THE GRID!)
        pass

    def update(self):
        # Function who update the game every tick
        pass

    def move_snake(self):
        # manage the position of the snake 
        pass

    def change_direction(self):
        # manage the change direction (NB: cannot change direction of 180 degrees!!)
        pass

    def check_collisions(self):
        # manage the collisions with the pitch or with himself
        pass

    def check_bomb_time(self):
        # delete the bomb after 10 seconds
        pass

    def spawn_bomb(self):
        # position of the bomb (free but not over the snake)
        pass