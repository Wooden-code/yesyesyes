# -*- coding = utf-8 -*-
# @Time : 5:06 下午
# @Author : 阿童木
# @File : sound.py
# @software: PyCharm
import pygame,sys

class Music_BG:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.game_info=None
    #背景音乐
    def update(self,surface,keys):#jinrule

        pygame.mixer.music.load("resource\music\渔舟唱晚.ogg")
        pygame.mixer.music.set_volume(1.0)#设置音量
        pygame.mixer.music.play(-1)#循环播放


    #特定音效

