# -*- encoding: gbk -*-

## 主要显示文字。关于游戏和操作说明

from util import *
import pygame
from pygame.locals import *
from sound import *

class Refer:
    def __init__(self,screen):
        self.screen = screen
        self.stat = 'help'
        self.screen.blit(pygame.image.load(
            file_path("background2.png")).convert(), (0, 0))

    def run(self):
        title = 'HELP'
        content = ['This is a game called "Break the Brick".',
                   'You need to collid all bricks by the ball',
                   'to be success.',
                   'Press SPACE to launch the ball. Use the',
                   'key LEFT and RIGHT to move the paddle.',
                   'Press ESCAPE to return to MENU.']
        myprint(self.screen,title,(240,30),'l')
        for i in xrange(len(content)):
            myprint(self.screen,content[i],(60,50*(i+1)+60))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            elif event.key == K_ESCAPE:
                bounce_sound()
                self.stat = 'menu'
            else:
                pass
        return self.stat
        
        
