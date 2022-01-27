import pygame

from boss_menu import BossMenu

class Main:
    def __init__(self):
        pygame.init()
        self.WINDOW_WIGHT = 600
        self.WINDOW_HEIGHT = 600
        self.screen = pygame.display.set_mode((self.WINDOW_HEIGHT, self.WINDOW_WIGHT))
        self.boss_menu = BossMenu()
        self.white = [255, 255, 255]


    def launch(self):
        while True:
            self.draw()
            self.screen.fill(self.white)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return 0

    def draw(self):
        self.boss_menu.draw_blocks(self.screen)

        pygame.display.flip()


main = Main()
main.launch()
