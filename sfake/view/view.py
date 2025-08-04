import os
import sys
import pygame

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600

class MenuView:
    button_width = 200
    button_height = 50
    center_x = SCREEN_WIDTH // 2 - button_width // 2
    showing_rules = False

    def __init__(self, game):
        pygame.init()
        self.font = pygame.font.SysFont("Arial", 36)

        self.showing_rules = False

        self.game = game
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, 600))
        pygame.display.set_caption("Snake Game")

        #Buttons
        self.button_start = pygame.Rect(self.center_x, 150, self.button_width, self.button_height)
        self.button_rules = pygame.Rect(self.center_x, 250, self.button_width, self.button_height)
        self.button_quit = pygame.Rect(self.center_x, 350, self.button_width, self.button_height)

        #Background
        base_path = os.path.dirname(os.path.abspath(__file__))
        self.background_image = pygame.image.load(
            os.path.join(base_path, "..", "..", "assets", "background.jpg")
        )

    def render(self):

        if not self.game.is_running:
            self.draw_menu()
        else:
            self.screen.blit(self.background_image, (0, 0))
            pygame.draw.rect(self.screen, (30, 30, 30), pygame.Rect(0, 0, 900, 60))
        pygame.display.flip()

    def draw_menu(self):
        self.screen.blit(self.background_image, (0, 0))
        self.draw_button(self.button_start, "Start", (0, 255, 0))
        self.draw_button(self.button_rules, "Rules", (0, 0, 255))
        self.draw_button(self.button_quit, "Quit", (255, 0, 0))

        if self.showing_rules:
            self.draw_rules_popup()

        pygame.display.flip()

    def draw_button(self, rect, text, color):
        pygame.draw.rect(self.screen, color, rect)
        label = self.font.render(text, True, (255, 255, 255))
        text_rect = label.get_rect(center=rect.center)
        self.screen.blit(label, text_rect)
    
    def draw_rules_popup(self):
        popup_rect = pygame.Rect(80, 80, 640, 400)
        pygame.draw.rect(self.screen, (30, 30, 30), popup_rect)
        pygame.draw.rect(self.screen, (255, 255, 255), popup_rect, 2)

        rules = [
            "Rules:",
            "1. Use arrows to move",
            "2. Eat food to grow",
            "3. Avoid crashing into walls or hitting yourself",
            "4. Avoid eating bombs",
            "5. Good Luck!"
        ]

        font = pygame.font.SysFont("Arial", 24)
        for i, line in enumerate(rules):
            txt = font.render(line, True, (255, 255, 255))
            self.screen.blit(txt, (popup_rect.x + 20, popup_rect.y + 30 + i * 30))

        # Draw OK button
        self.ok_button = pygame.Rect(popup_rect.centerx - 40, popup_rect.bottom - 60, 80, 40)
        pygame.draw.rect(self.screen, (0, 200, 0), self.ok_button)
        ok_text = font.render("OK", True, (255, 255, 255))
        self.screen.blit(ok_text, ok_text.get_rect(center=self.ok_button.center))


    def handle_click(self, mouse_pos, button_start, button_quit, button_rules):
        if self.showing_rules:
            if self.ok_button.collidepoint(mouse_pos):
                self.showing_rules = False
        elif button_start.collidepoint(mouse_pos):
            print("Start Game")
            self.game.start_game()

        elif button_rules.collidepoint(mouse_pos):
            print("Show Rules")
            self.showing_rules = True

        elif button_quit.collidepoint(mouse_pos):
            print("Quit Game")
            pygame.quit()
            sys.exit()
