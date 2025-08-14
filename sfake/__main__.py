import pygame
from sfake.controller.controller import InputController
from sfake.model.model import Game
from sfake.view.view import MenuView 


# this is the main module of your app
# it is only required if your project must be runnable
# this is the script to be executed whenever some users writes `python -m sfake` on the command line, eg.
def main():
    pygame.init()
    clock = pygame.time.Clock()

    game = Game()
    menu_view = MenuView(game)
    controller = InputController(game, menu_view)

    # Main loop
    running = True
    while running:
        controller.handle_input()  # Handles user input
        game.update()  # Updates the game state
        menu_view.render()  # Renders the current view
        clock.tick(15)

    pygame.quit()  # Closes Pygame


if __name__ == "__main__":
    main()