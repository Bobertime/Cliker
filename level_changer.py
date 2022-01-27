import pygame


class LevelChanger:
    def __init__(self, arrow_type):
        self.picture = pygame.image.load(f"img/{arrow_type}.png")
        self.step = -1 if arrow_type == "left" else 1
        self.pos = (0,0) if arrow_type == "left" else (500,0)

    def draw_block(self, screen):
        screen.blit(self.picture, self.pos)