# -*- encoding: gbk -*-
import pygame
from pygame.locals import *
from random import randint
from util import myprint
from sound import *

class Star:
    def __init__(self,x,y,speed):
        self.x = x
        self.y = y
        self.speed = speed

class Menu:
    title = str('Break the Bricks')
    opts = ['PLAY',
            'HELP',
            'QUIT']
    def __init__(self,screen):
        self.screen = screen
        self.number = 0
    
    def delete(self,star):
        return star.x > 0

    def run(self):
        pygame.init()
        clock = pygame.time.Clock()
        stars = []
        ## 动态背景
        for n in xrange(200):
            x = float(randint(0,639))
            y = float(randint(0,479))
            speed = float(randint(10,300))
            stars.append(Star(x,y,speed))
        
        while True:
            self.time_pass = clock.tick() / 1000.
            self.screen.fill((0,0,0))

            x = float(randint(0,639))
            speed = float(randint(10,300))
            if (x < 200. or x > 400.) and (y > 350 or y < 100):
                star = Star(x,0,speed)
                stars.append(star)
            for i in stars:
                new_y = i.y + self.time_pass * i.speed
                pygame.draw.aaline(self.screen,(255,255,255),
                                   (i.x,new_y),(i.x,i.y+1))
                i.y = new_y
            stars = filter(self.delete,stars)
        ## 菜单文字
            myprint(self.screen,self.title,(100,50),'l',(230,230,230))
            for i in xrange(len(self.opts)):
                if i == self.number:
                    myprint(self.screen,self.opts[i],(230,80*(i+1)+80),'l')
                else:
                    myprint(self.screen,self.opts[i],(240,80*(i+1)+80),
                            'm',(160,160,160))
        ## 用户输入
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                elif event.type == KEYDOWN:
                    bounce_sound()
                    if event.key == K_UP:
                        self.number = (self.number - 1) % len(self.opts)
                    elif event.key == K_DOWN:
                        self.number = (self.number + 1) % len(self.opts)
                    elif event.key == K_RETURN:
                        return self.opts[self.number].lower()  
            pygame.display.update()
