import pygame

from boss import Boss
from boss_menu import BossMenu
from level_changer import LevelChanger


class Main:
    def __init__(self):
        pygame.init()
        self.WINDOW_WIGHT = 600
        self.WINDOW_HEIGHT = 600
        self.screen = pygame.display.set_mode((self.WINDOW_HEIGHT, self.WINDOW_WIGHT))
        self.boss_menu = BossMenu()
        self.active_boss_level = 1
        self.boss = Boss(self.active_boss_level, 100)
        self.white = [255, 255, 255]

    def launch(self):
        while True:
            self.draw()
            self.screen.fill(self.white)
            pygame.draw.rect(self.screen, [123, 123, 132], (50, 100, 500, 500), 0)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return 0
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.try_to_click(event.pos)
                    if event.button == 1:
                        # if event.pos == self.:
                        self.boss.attack(self.active_boss_level, self.screen)

    def draw(self):
        self.boss_menu.draw_blocks(self.screen)
        self.boss.draw_boss(self.screen)
        self.boss.hp_boss(1, self.screen)
        pygame.display.flip()

    def try_to_click(self, pos):
        for block in self.boss_menu.blocks:
            if block.is_clicked(pos):
                if isinstance(block, LevelChanger):
                    self.boss_menu.change_boss_info(block.step)
                    break


main = Main()
main.launch()
