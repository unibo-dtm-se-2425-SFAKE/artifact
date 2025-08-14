import sys
import pygame

class InputController:
    def __init__(self, game, view):
        self.game = game
        self.view = view

    def handle_input(self):
        #Cycle through all events

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #Handle window close event
                pygame.quit()
                sys.exit()
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                #Handle mouse button clicks on the menu buttons
                if not self.game.is_running:
                    self.view.handle_click(
                        event.pos, 
                        self.view.button_start, 
                        self.view.button_quit,
                        self.view.button_rules
                    )
            elif event.type == pygame.KEYDOWN and self.game.is_running:
                #Handle key presses for snake movement
                # Check for arrow keys to change direction

                if event.key == pygame.K_UP and self.game.direction != (0, 15):
                    self.game.change_direction(0, -15)

                elif event.key == pygame.K_DOWN and self.game.direction != (0, -15):
                    self.game.change_direction(0, 15)

                elif event.key == pygame.K_LEFT and self.game.direction != (15, 0):
                    self.game.change_direction(-15, 0)

                elif event.key == pygame.K_RIGHT and self.game.direction != (-15, 0):
                    self.game.change_direction(15, 0)