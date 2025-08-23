import unittest
from unittest.mock import MagicMock, patch
import pygame
from sfake.controller.controller import InputController

class TestInputController(unittest.TestCase):
    def setUp(self):
        self.game = MagicMock()
        self.view = MagicMock()
        self.controller = InputController(self.game, self.view)

    @patch('pygame.event.get')
    def test_handle_input_quit_event(self, mock_event_get):
        mock_event_get.return_value = [pygame.event.Event(pygame.QUIT)]
        with patch('pygame.quit') as mock_quit, patch('sys.exit') as mock_exit:
            self.controller.handle_input()
            mock_quit.assert_called_once()
            mock_exit.assert_called_once()

    #TODO
    @patch('pygame.event.get')
    def test_handle_input_mouse_button_down(self, mock_event_get):
        self.game.is_running = False
        mock_event_get.return_value = [pygame.event.Event(pygame.MOUSEBUTTONDOWN, {'pos': (100, 100)})]
        self.controller.handle_input()
        self.view.handle_click.assert_called_once()

    @patch('pygame.event.get')
    def test_handle_input_keydown_up(self, mock_event_get):
        self.game.is_running = True
        self.game.direction = (0, 0)
        mock_event_get.return_value = [pygame.event.Event(pygame.KEYDOWN, {'key': pygame.K_UP})]
        self.controller.handle_input()
        self.game.change_direction.assert_called_with(0, -15)

    @patch('pygame.event.get')
    def test_handle_input_keydown_down(self, mock_event_get):
        self.game.is_running = True
        self.game.direction = (0, 0)
        mock_event_get.return_value = [pygame.event.Event(pygame.KEYDOWN, {'key': pygame.K_DOWN})]
        self.controller.handle_input()
        self.game.change_direction.assert_called_with(0, 15)

    @patch('pygame.event.get')
    def test_handle_input_keydown_left(self, mock_event_get):
        self.game.is_running = True
        self.game.direction = (0, 0)
        mock_event_get.return_value = [pygame.event.Event(pygame.KEYDOWN, {'key': pygame.K_LEFT})]
        self.controller.handle_input()
        self.game.change_direction.assert_called_with(-15, 0)

    @patch('pygame.event.get')
    def test_handle_input_keydown_right(self, mock_event_get):
        self.game.is_running = True
        self.game.direction = (0, 0)
        mock_event_get.return_value = [pygame.event.Event(pygame.KEYDOWN, {'key': pygame.K_RIGHT})]
        self.controller.handle_input()
        self.game.change_direction.assert_called_with(15, 0)

if __name__ == '__main__':
    unittest.main()