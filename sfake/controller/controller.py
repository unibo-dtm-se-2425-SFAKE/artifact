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
                #Handle mouse button clicks

                if not self.game.is_running:
                    self.view.handle_click(
                        event.pos, 
                        self.view.button_start, 
                        self.view.button_quit,
                        self.view.button_rules
                    )
            elif event.type == pygame.KEYDOWN and self.game.is_running: #TEST WORKING EVENT
                if event.key == pygame.K_UP:
                    pygame.quit()
                    sys.exit()  # Exit the game
                