# -*- coding = utf-8 -*-
# @Time : 7:12 下午
# @Author : 阿童木
# @File : info.py
# @software: PyCharm
#文字信息
import pygame
from .. import constants as C
from . import coin
from .. import setup,tools
pygame.font.init()

class Info:
    def __init__(self,state,game_info):#初始化 state阶段，以便管理各个阶段
        self.state=state
        self.game_info=game_info
        self.create_state_labels()
        self.create_info_labels()
        self.flash_coin=coin.FlashingCoin()

    def create_state_labels(self):#创作某个阶段特有的文字，分数，金币，时间，等信息
        self.state_labels=[]
        if self.state=='main_menu':#如果是主菜单阶段
            self.state_labels.append((self.create_label('1 PLAYER GAME'),(272,360)))
            self.state_labels.append((self.create_label('2 PLAYERS GAME'),(272,405)))
            self.state_labels.append((self.create_label('TOP - '),(290,465)))
            self.state_labels.append((self.create_label('000000'),(400,465)))
        elif self.state=='load_screen':#加载页面
            self.state_labels.append((self.create_label('WORLD'), (280, 200)))
            self.state_labels.append((self.create_label('1 - 1'), (430, 200)))
            self.state_labels.append((self.create_label('X    {}'.format(self.game_info['lives'])), (380, 280)))

        elif self.state=='game_over':
            self.state_labels.append((self.create_label('GAME OVER'), (280, 300)))


    def create_info_labels(self):
        self.info_labels=[]
        self.info_labels.append((self.create_label('MARIO'), (75,30)))
        self.info_labels.append((self.create_label('WORLD'), (450, 30)))
        self.info_labels.append((self.create_label('TIME'), (625, 30)))
        self.info_labels.append((self.create_label('000000'), (75, 55)))
        self.info_labels.append((self.create_label('x00'), (300, 55)))
        self.info_labels.append((self.create_label('1 - 1'), (480, 55)))

    def create_label(self,label,size=40,width_scale=1.25,height_scale=1):#调整字
        font=pygame.font.SysFont(C.FONT,size)
        label_image=font.render(label,1,(255,255,255))#把文字渲染成图片 白 理论上这里的1能够产生锯齿效果，但效果不明显，所以用以下方法
        rect=label_image.get_rect()#先把字体变小产生图片
        label_image=pygame.transform.scale(label_image,(int(rect.width*width_scale),int(rect.height*height_scale)))#放大产生锯齿效果


        return label_image

    def update(self):#不断更新时间，分数这样
        self.flash_coin.update()

    def draw(self,surface):#绘画
        for label in self.state_labels:
            surface.blit(label[0],label[1])#用blit方法画出来 对应 图片，位置
        for label in self.info_labels:
            surface.blit(label[0],label[1])
        surface.blit(self.flash_coin.image,self.flash_coin.rect)

