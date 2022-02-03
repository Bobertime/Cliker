import pygame


class LevelChanger:
    def __init__(self, arrow_type):
        self.picture = pygame.image.load(f"img/{arrow_type}.png")
        self.step = -1 if arrow_type == "left" else 1
        self.pos = (0, 0) if arrow_type == "left" else (500, 0)
        self.WIDTH = 100
        self.HEIGHT = 100

    def draw_block(self, screen):
        screen.blit(self.picture, self.pos)

    def is_clicked(self, pos):
        return self.pos[0] < pos[0] < self.pos[0] + self.WIDTH and \
                self.pos[1] < pos[1] < self.pos[1] + self.HEIGHT
