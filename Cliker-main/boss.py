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

    def hp_boss(self, health, screen):
        f1 = pygame.font.Font(None, 36)
        text1 = f1.render("HP  " + str(self.health), True,
                          (0, 0, 0))
        screen.blit(text1, (515, 300))

    def attack(self, health, screen):
        f1 = pygame.font.Font(None, 36)
        if self.health != 0:
            self.health -= 1
        elif self.health == 0:
            text1 = f1.render("HP" + str("Вы смогли!"), True, (0, 0, 0))
            screen.blit(text1, (515, 300))
