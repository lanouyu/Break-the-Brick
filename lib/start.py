# -*- encoding: gbk -*-

import pygame
import util,sound
from pygame.locals import *
from menu import *
import game
import refer

class Start:
    def __init__(self):
        ## 初始状态为选择菜单
        self.stat = 'menu'
        ## 初始化
        pygame.mixer.pre_init(44100,16,2,1024*4)
        pygame.init()
        ## 窗口
        pygame.display.set_caption('Break the Brick')
        self.init()
        try:
            self.screen = pygame.display.set_mode((640, 480), 
                    HWSURFACE | SRCALPHA, 32)
        except:
            self.screen = pygame.display.set_mode((640, 480), 
                    SRCALPHA, 32)
        ## 创建menu和main的实例
        self.menu = Menu(self.screen)

    def init(self):
        ## 初始化文字和音乐
        util.init()
        sound.load()

    def loop(self):
        clock = pygame.time.Clock()
        while self.stat != 'quit':
            if self.stat == 'menu':
                self.stat = self.menu.run()
            elif self.stat == 'play':
                self.stat = game.Game(self.screen).run()
            elif self.stat == 'help':
                self.stat = refer.Refer(self.screen).run()
            pygame.display.update()
        pygame.quit()

def run():
    start = Start()
    start.loop()

if __name__ == '__main__':
    print 'RUN "run_game.py" PLEASE !'

            
                
            
        
