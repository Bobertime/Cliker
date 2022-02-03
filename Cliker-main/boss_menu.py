import pygame

from boss import Boss
from level_changer import LevelChanger


class BossMenu:
    def __init__(self):
        self.blocks = []
        self.fill_boos_info()
        self.fill_level_changer()

    def fill_boos_info(self):
        for i in range(1, 5):
            self.blocks.append(Boss(i, i * 100))

    def fill_level_changer(self):
        self.blocks.insert(0, LevelChanger("left"))
        self.blocks.append(LevelChanger("right"))

    def draw_blocks(self, screen):
        for block in self.blocks:
            block.draw_block(screen)

    def change_boss_info(self, step):
        if step == -1:
            self.change_boss_info_to_the_left()
        else:
            self.change_boss_info_to_the_right()

    def change_boss_info_to_the_left(self):
        if self.blocks[1].level == 1:
            return
        self.blocks.pop(-2)
        self.blocks.insert(1, Boss(self.blocks[1].level - 1, 100))
        for i in range(2, 5):
            self.blocks[i].block_pos[0] += 100

    def change_boss_info_to_the_right(self):
        self.blocks.pop(1)
        self.blocks.insert(-1, Boss(self.blocks[-2].level + 1, 400))
        for i in range(1, 4):
            self.blocks[i].block_pos[0] -= 100
