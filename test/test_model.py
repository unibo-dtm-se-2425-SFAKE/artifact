import unittest
from sfake.model.model import Game

class TestModel(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_food_on_grid(self):
        # Verifica che il cibo generato sia allineato alla griglia 15x15
        food = self.game.generate_food()
        self.assertEqual(food[0] % 15, 0)
        self.assertEqual(food[1] % 15, 0)

    def test_food_within_bounds(self):
        # Verifica che il cibo venga generato all'interno dei limiti del campo di gioco
        food = self.game.generate_food()
        self.assertGreaterEqual(food[0], 0)
        self.assertLess(food[0], 900)
        self.assertGreaterEqual(food[1], 60)
        self.assertLess(food[1], 600)

    def test_food_on_snake(self):
        # Verifica che il cibo non venga generato sopra il corpo del serpente
        self.game.snake = [(225, 225), (210, 225), (195, 225)]
        for _ in range(100):
            food = self.game.generate_food()
            self.assertNotIn(food, self.game.snake)

    def test_move(self):
        # Verifica che il serpente si muova correttamente in avanti
        initial_head = self.game.snake[0]
        self.game.move_snake()
        new_head = self.game.snake[0]
        self.assertEqual(new_head, (initial_head[0] + 15, initial_head[1]))

    def test_snake_collision_self(self):
        # Simula una situazione in cui il serpente collide con sé stesso
        self.game.snake = [(100, 100), (85, 100), (70, 100), (70, 115), (85, 115), (100, 115), (100, 100)]
        self.game.check_collisions()
        self.assertTrue(self.game.is_game_over)

    def test_collision_wall(self):
        # Simula una situazione in cui il serpente colpisce il bordo del campo
        self.game.snake = [(900, 100)]  # Fuori dal bordo destro
        self.game.check_collisions()
        self.assertTrue(self.game.is_game_over)

    def test_food_collision(self):
        # Verifica che il punteggio aumenti correttamente quando il serpente mangia la mela
        self.game.food = (self.game.snake[0][0] + 15, self.game.snake[0][1])
        self.game.move_snake()
        self.assertEqual(self.game.score, 1)

    def test_game_reset(self):
        # Verifica che il reset del gioco riporti tutti i parametri allo stato iniziale
        self.game.score = 5
        self.game.snake = [(0, 0)]
        self.game.is_game_over = True
        self.game.start_game()
        self.assertFalse(self.game.is_game_over)
        self.assertEqual(self.game.snake, [(225, 225), (210, 225), (195, 225)])
        self.assertEqual(self.game.score, 0)

    def test_change_directions(self):
        self.game.change_direction(0, -15)
        self.assertEqual(self.game.direction, (0, -15))
        self.game.change_direction(0, 15)
        self.assertNotEqual(self.game.direction, (0, 15))

    def test_update(self):
        self.game.start_game()
        head = self.game.snake[0]
        self.game.update()
        self.assertNotEqual(self.game.snake[0], head)

if __name__ == '__main__':
    unittest.main()
