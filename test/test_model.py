import unittest
from unittest.mock import patch, MagicMock
import pygame
from sfake.controller.controller import InputController

class TestInputController(unittest.TestCase):

    def setUp(self):
        # Setup iniziale con mock di game e view e istanza di InputController
        pass

    @patch('pygame.event.get')
    def test_handle_input_quit_event(self, mock_event_get):
        #TODO: Verifica che alla chiusura della finestra pygame.quit e sys.exit vengano chiamati
        pass

    @patch('pygame.event.get')
    def test_handle_input_mouse_button_down(self, mock_event_get):
        #TODO: Verifica che quando clicchi il mouse chiami la funzione di gestione click dei bottoni nella view
        pass

    @patch('pygame.event.get')
    def test_handle_input_keydown_up(self, mock_event_get):
        # TODO: Verifica che premendo la freccia SU poi la direzione diventi SU
        pass

    @patch('pygame.event.get')
    def test_handle_input_keydown_down(self, mock_event_get):
        # TODO: Verifica che premendo la freccia GIU poi la direzione diventi GIU
        pass

    @patch('pygame.event.get')
    def test_handle_input_keydown_left(self, mock_event_get):
        # TODO: Verifica che premendo la freccia SX poi la direzione diventi SX
        pass

    @patch('pygame.event.get')
    def test_handle_input_keydown_right(self, mock_event_get):
        # TODO: Verifica che premendo la freccia DX poi la direzione diventi DX
        pass

if __name__ == '__main__':
    unittest.main()
