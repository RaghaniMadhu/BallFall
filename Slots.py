import pygame


class Slot:
    def __init__(self, value, color, top_left_x, top_left_y, width, height, slot_id=None):
        self.value = value
        self.color = color
        self.x_position = top_left_x
        self.y_position = top_left_y
        self.width = width
        self.height = height
        self.slot_id = slot_id

    def draw_slot(self, surface):
        self.slot_id = pygame.draw.rect(surface, self.color,[self.x_position, self.y_position, self.width, self.height])

    def refresh_slot(self):
        pygame.display.update(self.slot_id)
