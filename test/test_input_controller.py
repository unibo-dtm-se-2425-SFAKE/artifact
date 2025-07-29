import unittest
from snake.model.game import Game

class TestModel(unittest.TestCase):

    def setUp(self):
        # Setup iniziale con l'istanza di Game
        pass

    def test_food_on_grid(self):
        # TODO: Verifica che il cibo generato sia in linea con la griglia 15x15
        pass

    def test_food_within_bounds(self):
        # TODO: Verifica che il cibo venga generato dentro il  campo di gioco
        pass

    def test_food_on_snake(self):
        # TODO: Verifica che il cibo non venga generato sopra il serpente
        pass

    def test_move(self):
        # TODO: Verifica che il serpente si muova correttamente in avanti
        pass

    def test_snake_collision_self(self):
        # TODO: Simula una situazione in cui il serpente mangia se stesso
        pass

    def test_collision_wall(self):
        # TODO: Simula una situazione in cui il serpente si schianta con il bordo
        pass

    def test_food_collision(self):
        # TODO: Verifica che il punteggio aumenti correttamente quando il serpente mangia la mela
        pass

    def test_game_reset(self):
        # TODO: Verifica che il reset del gioco riporti tutti i parametri allo stato iniziale
        pass

    def test_change_directions(self):
        # TODO: Verifica il corretto cambio di direzione (evitando esempio che da destra vada a sinistra)
        pass

    def test_update(self):
        # TODO: Verifica che la funzione update modifichi la posizione del serpente
        pass

if __name__ == '__main__':
    unittest.main()
