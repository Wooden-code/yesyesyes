# -*- coding = utf-8 -*-
# @Time : 5:06 下午
# @Author : 阿童木
# @File : tools.py
# @software: PyCharm
# 工具和游戏主控
import sys
from PIL import Image
import pygame
import os
import random


class Game:


    # @staticmethod
    # def get_instance():
    #     if Game.instance == None:
    #         Game.instance = Game()
    #     return Game.instance

    def __init__(self,state_dict,start_state):
        #pygame.init()
        #pygame.display.set_mode((800, 600))
        self.screen = pygame.display.get_surface()
        self.clock = pygame.time.Clock()  # 计时控制帧数

        self.state_dict=state_dict
        self.state=self.state_dict[start_state]

    def update(self):
        keys = pygame.key.get_pressed()
        if self.state.finished:#先判断当前阶段有没有完结
            game_info=self.state.game_info
            next_state=self.state.next
            self.state.finished=False
            self.state=self.state_dict[next_state]
            self.state.start(game_info)
        self.state.update(self.screen,keys)



    def run(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    self.keys = pygame.key.get_pressed()#keys按键
                elif event.type == pygame.KEYUP:
                    self.keys == pygame.key.get_pressed()
            self.update()
            '''
            self.screen.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))  # 不断随机填充颜色
            image=get_image(GRAPHICS['mario_bros.png'],145,32,16,16,(0,0,0),5) #x，y，宽，高，抠图底色，放大倍数
            self.screen.blit(image,(300,300))
            '''
            #print(state,id(state))
            #state.get_instance().update(self.screen,self.keys)

            #state.get_instance().update(self.screen, self.keys)
            #state().update(self.screen,self.keys)#如果state后面的圆括号不加会报后面的错误。对象的声明需要括号，而类的声明括号可有可无，TypeError: update() missing 1 required positional argument: 'surface'
            #state.update(self)

            pygame.display.update()
            self.clock.tick(60)  # 每秒六十帧 越大越流畅，但电脑负荷也就越大


def load_graphics(path):
        graphics = {}
        for pic in os.listdir(path):
            try :


                 img = pygame.image.load(os.path.join(path, pic))
                 if img.get_alpha():  # 如果是透明底的

                     img = img.convert_alpha()
                 else:
                     img = img.convert_alpha()
                 graphics[pic] = img
            except:
                pass
        return graphics


def get_image(sheet, x, y, width, height, colorkey, scale):#colorkey是抠图的底色，scale是放大倍数
        image = pygame.Surface((width, height))
        image.blit(sheet, (0, 0), (x, y, width, height))#xywh代表从哪里取下这个sheet
        image.set_colorkey(colorkey)#快速抠图
        image = pygame.transform.scale(image, (int(width * scale),int(height * scale)))#放大图片
        return image

import pygame as py
from pygame.locals import *
import sys

def button(x,y,w,h):
    mouse_x,mouse_y=pygame.mouse.get_pos()
    mouse=pygame.mouse.get_pressed()#这个w不是纯纯wide而是x坐标加上宽度的w
    clock=pygame.time.Clock()
    clock.tick(300)

    if x<mouse_x < w and y<mouse_y <h :
        if mouse==(0,0,0):
            return 10
        elif mouse==(1,0,0):#dianji
            return 8
        else:
            return 6

