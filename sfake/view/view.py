import os
import sys
import pygame

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 50

class MenuView:
    center_x = SCREEN_WIDTH // 2 - BUTTON_WIDTH // 2
    showing_rules = False

    def __init__(self, game):
        pygame.init()
        self.font = pygame.font.SysFont("Arial", 36)
        
        self.showing_rules = False
        self.game = game
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, 600))
        pygame.display.set_caption("Sfake Game")

        #Buttons
        self.button_start = pygame.Rect(self.center_x, 150, BUTTON_WIDTH, BUTTON_HEIGHT)
        self.button_rules = pygame.Rect(self.center_x, 250, BUTTON_WIDTH, BUTTON_HEIGHT)
        self.button_quit = pygame.Rect(self.center_x, 350, BUTTON_WIDTH, BUTTON_HEIGHT)

        #Background
        base_path = os.path.dirname(os.path.abspath(__file__))
        self.background_image = pygame.image.load(os.path.join(base_path, "..", "..", "assets", "background.jpg"))

        self.apple_image = pygame.image.load(os.path.join(base_path, "..", "..", "assets", "apple.png"))
        self.apple_image = pygame.transform.scale(self.apple_image,(15, 15))

        self.bomb_image = pygame.image.load(os.path.join(base_path, "..", "..", "assets", "bomb.png"))
        self.bomb_image = pygame.transform.scale(self.bomb_image,(15, 15))

    def render(self):
        self.screen.blit(self.background_image, (0, 0))
        pygame.draw.rect(self.screen, (30, 30, 30), pygame.Rect(0, 0, SCREEN_WIDTH, 60))

        if not self.game.is_running:
            if self.game.is_game_over:
                self.draw_game_over()
            else: 
                self.draw_menu()
        else:
            self.draw_snake()
            self.draw_food()
            if self.game.bomb:
                self.draw_bomb()
            self.draw_score()
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

        #Draw OK button
        self.ok_button = pygame.Rect(popup_rect.centerx - 40, popup_rect.bottom - 60, 80, 40)
        pygame.draw.rect(self.screen, (0, 200, 0), self.ok_button)
        ok_text = font.render("OK", True, (255, 255, 255))
        self.screen.blit(ok_text, ok_text.get_rect(center=self.ok_button.center))

    def draw_snake(self):
        for segment in self.game.snake:
            pygame.draw.rect(self.screen, (0, 255, 0), pygame.Rect(segment[0], segment[1], 15, 15))

    def draw_food(self):
        self.screen.blit(self.apple_image, self.game.food)

    def draw_bomb(self):
        self.screen.blit(self.bomb_image, self.game.bomb)

    def draw_score(self):
        score_text = self.font.render(f"Score: {self.game.score}", True, (255, 255, 255))
        text_rect = score_text.get_rect(center=(450, 25))
        self.screen.blit(score_text, text_rect)
    
    def draw_game_over(self):
        over_text = self.font.render("You died!!", True, (255, 0, 0))
        score_text = self.font.render(f"Score: {self.game.score}", True, (255, 255, 255))
        self.screen.blit(over_text, over_text.get_rect(center=(450, 250)))
        self.screen.blit(score_text, score_text.get_rect(center=(450, 300)))

        self.menu_button = pygame.Rect(450 - 100, 400, 200, 50)
        pygame.draw.rect(self.screen, (30, 30, 30), self.menu_button)
        menu_text = self.font.render("Menu", True, (255, 255, 255))
        self.screen.blit(menu_text, menu_text.get_rect(center=self.menu_button.center))

    def handle_click(self, mouse_pos, button_start, button_quit, button_rules):
        if self.showing_rules:
            if self.ok_button.collidepoint(mouse_pos):
                self.showing_rules = False

        elif self.game.is_game_over:
            if hasattr(self, 'menu_button') and self.menu_button.collidepoint(mouse_pos):
                self.game.is_game_over = False
                self.showing_rules = False
                self.game.is_running = False

        elif button_start.collidepoint(mouse_pos):
            self.game.start_game()

        elif button_rules.collidepoint(mouse_pos):
            self.showing_rules = True

        elif button_quit.collidepoint(mouse_pos):
            pygame.quit()
            sys.exit()
