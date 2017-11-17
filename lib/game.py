# -*- encoding: gbk -*-
import pygame
from pygame.locals import *
from util import *
from sound import *

class Game():
    def __init__(self,screen):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.stat = 'play'
        self.screen = screen
        self.screen_size = (640,480)
        self.brick_w = 60
        self.brick_h= 15
        self.paddle_w = 60
        self.paddle_h = 15
        self.ball_d = 18
        self.ball_r = self.ball_d / 2
        self.ball_v = [1,-1]
        self.paddle_maxx = self.screen_size[0] - self.paddle_w
        self.paddle_maxy = self.screen_size[1] - self.paddle_h - 25 
        self.ball_maxx = self.screen_size[0] - self.ball_d
        self.ball_maxy = self.screen_size[1] - self.ball_d
        self.lives = 3
        self.score = 0
        self.speed = 5
        self.paddle = pygame.Rect(290,self.paddle_maxy,self.paddle_w,self.paddle_h)
        self.ball = pygame.Rect(310,self.paddle_maxy - self.ball_d,self.ball_d,self.ball_d)
        self.state = 'PREPARE'

        self.layout()

    ## 砖块布局
    def layout(self):
        self.pos_y = 40
        self.bricks = []
        for i in range(10):
            self.pos_x = 40
            for j in range(8):
                self.bricks.append(pygame.Rect(self.pos_x,self.pos_y,self.brick_w,self.brick_h))
                self.pos_x += self.brick_w + 10
            self.pos_y += self.brick_h + 5
        del self.bricks[-21:-19],self.bricks[-14:-10],self.bricks[-7:-1]

    ## 屏幕显示
    def draw(self):
        ## 图形绘制
        i = 0
        for brick in self.bricks:
            i += 1
            self.color = (200,100+i,0)
            pygame.draw.rect(self.screen,self.color,brick)

        pygame.draw.rect(self.screen,(100,100,250),self.paddle,4)
        pygame.draw.circle(self.screen,(255,255,255),
                           (self.ball.x,self.ball.y + self.ball_r),self.ball_r)
        ## 文字显示
        myprint(self.screen,"SCORE: " + str(self.score)
                + " LIVES: " + str(self.lives),(380,5))
        myprint(self.screen,"UP to pause; ESCAPE to menu",(0,450))

    def move(self):
        self.ball.x += self.ball_v[0] * self.speed
        self.ball.y += self.ball_v[1] * self.speed
        ## 碰壁反向
        if self.ball.x <= 0:
            self.ball.x = 0
            bounce_sound()
            self.ball_v[0] = -self.ball_v[0]
        elif self.ball.x >= self.ball_maxx:
            self.ball.x = self.ball_maxx
            bounce_sound()
            self.ball_v[0] = -self.ball_v[0]
        if self.ball.y < 40:
            self.ball.y = 40
            bounce_sound()
            self.ball_v[1] = -self.ball_v[1]

    def react(self):
        ## 对碰撞的反应
        for i in self.bricks:
            if self.ball.colliderect(i):
                bounce_sound()
                self.score += 2
                self.ball_v[1] = -self.ball_v[1]
                self.bricks.remove(i)
        if self.ball.colliderect(self.paddle):
            bounce_sound()
            self.ball.y = self.paddle_maxy - self.ball_d
            self.ball_v[1] = -self.ball_v[1]
        ## 对游戏进程状态的反应
        if self.ball.y > self.paddle.y:
            self.lives -= 1
            bounce_sound()
            if self.lives > 0:
                self.score -= 5
                self.state = 'PREPARE'
            else:
                self.state = 'GAMEOVER'
        if len(self.bricks) == 0:
            self.state = 'WON'

    ## 用户输入
    def put_in(self):
        self.stat = 'play'
        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            self.paddle.x -= self.speed
            if self.paddle.x < 0:
                self.paddle.x = 0
        elif keys[K_RIGHT]:
            self.paddle.left += self.speed
            if self.paddle.x > self.paddle_maxx:
                self.paddle.x = self.paddle_maxx

        if keys[K_SPACE] and self.state == 'PREPARE':
            self.ball_v = [1,-1]
            bounce_sound()
            self.state = 'PLAYING'
        elif keys[K_UP] and self.state == 'PLAYING':
            self.state = 'PREPARE'
            bounce_sound()
        return self.stat
    
    def run(self):
        while self.stat == 'play':
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                elif event.key == K_ESCAPE:
                    bounce_sound()
                    self.stat = 'menu'
                    return self.stat

            self.clock.tick(50)
            self.screen.blit(pygame.image.load(
                file_path("background1.png")).convert(),(0, 0))
            self.put_in()
            self.draw()

            if self.state == 'PLAYING':
                self.move()
                self.react()
            elif self.state == 'PREPARE':
                self.ball.x = self.paddle.x + self.paddle_w / 2
                self.ball.y = self.paddle.y - self.ball_d
                self.screen.blit(pygame.image.load(
                    file_path("prepare.png")).convert_alpha(), (40,260))
            elif self.state == 'GAMEOVER':
                self.screen.blit(pygame.image.load(
                    file_path("gameover.png")).convert_alpha(), (40,260))
                myprint(self.screen,'GAME OVER',(140,200),'l')
            elif self.state == 'WON':
                self.screen.blit(pygame.image.load(
                    file_path("win.png")).convert_alpha(), (40,260))
                myprint(self.screen,'CONGRATULATIONS',(80,200),'l')

            pygame.display.flip()
