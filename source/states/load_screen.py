# -*- coding = utf-8 -*-
from ..components import info
import pygame,math
import time
from .. import setup
from .. import constants as C
from ..components import info
import os

def wrap_angle(angle):
    return angle

def gogo(num):
    if num == 1:
        fii = 'eat.ogg'
    elif num == 2:
        fii = 'drop.ogg'
    abs = os.getcwd()
    sds = abs.split(r'\\')
    ewr = sds[0] + r'\\resource\\music\\' + fii
    try:
        pygame.mixer.Sound(ewr).play()
    except:
        ewr = sds[0].split('dist')[0] + r'resource\\music\\' + fii
        pygame.mixer.Sound(ewr).play()
    return 0

class LoadScreen:
    angle = 0
    def start(self,game_info):
        self.game_info=game_info
        self.info=info.Info('load_screen',game_info)
        self.finished=False
        self.next='level'
        self.duration=2000
        self.timer=0
        self.info=info.Info('load_screen',self.game_info)
        abs = os.getcwd()
        sds = abs.split(r'\\')
        ewr = r'\\'.join(sds) + r'\\resource\\music\\start.ogg'
        pygame.mixer.music.load(ewr)  # 方法问题
        pygame.mixer.music.set_volume(1.0)  # 设置音量
        pygame.mixer.music.play(-1)  # 循环播放
        #pygame.mixer.music.load(os.path.abspath("resource/music/start.ogg"))


    def update(self,surface,keys):

        surface=pygame.display.set_mode((1200,900))
        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse = pygame.mouse.get_pressed()
        tips_3 = setup.GRAPHICS['tips_3.png']
        tips_2 = setup.GRAPHICS['tips_2.png']
        tips_1 = setup.GRAPHICS['tips_1.png']
        fonts_1=setup.GRAPHICS['font.png']
        self.setup_background()
        surface.blit(self.background, self.viewport)
        LoadScreen.angle = wrap_angle(LoadScreen.angle - 1)
        rtips_1=pygame.transform.rotate(tips_1, abs(math.sin(math.radians(LoadScreen.angle))*10))
        rtips_2=pygame.transform.rotate(tips_2, abs(math.sin(math.radians(LoadScreen.angle))*10))
        rtips_3=pygame.transform.rotate(tips_3, abs(math.sin(math.radians(LoadScreen.angle))*10))
        if 209 < mouse_x < 289 and 313 < mouse_y < 519:
            if mouse == (0, 0, 0):
                surface.blit(rtips_1, (218, 295))
                surface.blit(fonts_1,(330,50))
                surface.blit(tips_3, (841, 300))
                surface.blit(tips_2, (560, 330))
                pygame.display.update()
            elif mouse == (1, 0, 0):
                self.finished=True
                '''
        elif 560 < mouse_x < 640 and 343 < mouse_y < 549:
           if mouse == (0, 0, 0):
               surface.blit(rtips_2, (560, 330))
               surface.blit(fonts_1,(330,50))
               surface.blit(tips_3, (841, 300))
               surface.blit(tips_1, (218, 295))
               pygame.display.update()
           elif mouse == (1, 0, 0):
               surface.blit(tips_2, (560, 330))
               surface.blit(fonts_1,(330,50))
               surface.blit(tips_3, (841, 300))
               surface.blit(tips_1, (218, 295))
               pygame.display.update()
        elif 841 < mouse_x < 921 and 313 < mouse_y < 519:
           if mouse == (0, 0, 0):
               surface.blit(rtips_3, (841, 300))
               surface.blit(fonts_1,(330,50))
               surface.blit(tips_2, (560, 330))
               surface.blit(tips_1, (218, 295))
               pygame.display.update()
           elif mouse == (1, 0, 0):
               self.finished=True
               '''
        elif 560 < mouse_x < 640 and 800 < mouse_y < 1000:
            surface.blit(tips_3, (841, 300))
            surface.blit(tips_2, (560, 330))
            surface.blit(tips_1, (218, 295))
            if mouse == (1, 0, 0):
                sys.exit()
        else:
            surface.blit(tips_3, (841, 300))
            surface.blit(tips_2, (560, 330))
            surface.blit(tips_1, (218, 295))



    def setup_background(self):  # 设置底图
        self.background = setup.GRAPHICS['rrtt.png']
        self.background_rect = self.background.get_rect()
        self.background = pygame.transform.scale(self.background, (
            int(self.background_rect.width * C.BG_W_MULTI), int(self.background_rect.height * C.BG_H_MULTI)))
        self.viewport = setup.SCREEN.get_rect()  # 滑动窗口

class GameOver(LoadScreen):
    def start(self,game_info):#由于gameover不再从loadscreen继承init类，所以下面参数都要补上
        self.game_info=game_info
        self.finished=False
        self.next='main_menu'
        self.duration=4000
        self.timer=0
        self.info=info.Info('game_over',self.game_info)