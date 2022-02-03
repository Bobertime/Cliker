import pygame.image


class Boss:
    def __init__(self, level, block_pos):
        self.level = level
        self.health = level * 50
        self.gold = level * 2

        self.font = pygame.font.SysFont("arial", 30)
        self.block_picture = self.font.render(str(level), False, (0, 0, 255))
        self.block_pos = [block_pos + 30, 30]

        self.picture = pygame.image.load("img/boss.png")
        self.pos = (100, 100)

    def draw_block(self, screen):
        screen.blit(self.block_picture, self.block_pos)

    def draw_boss(self, screen):
        screen.blit(self.picture, self.pos)

    def is_clicked(self, pos):
        return False
