import pygame

class Surface:
    def __init__(self, resolution, title, color=None):
        self.game_display = pygame.display.set_mode(resolution, pygame.RESIZABLE)
        self.screen = None
        pygame.display.set_caption(title)  # Title Of The Window
        self.screen_color = color

    def draw_surface(self):
        self.screen = self.game_display.fill(self.screen_color)

    def refresh_background(self):
        pygame.display.update(self.screen)
