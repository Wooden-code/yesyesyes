
import pygame,sys,os

class Music_BG:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.game_info=None
    #背景音乐
    def update(self,surface,keys):#jinrule
        pygame.mixer.music.load(os.path.abspath("resource/music/渔舟唱晚.ogg"))#方法问题
        pygame.mixer.music.set_volume(1.0)#设置音量
        pygame.mixer.music.play(-1)#循环播放


    #特定音效

