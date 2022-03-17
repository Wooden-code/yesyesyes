# -*- coding = utf-8 -*-
from ..components import info
import pygame,math
import time
from .. import setup
from .. import constants as C
from ..components import info

def wrap_angle(angle):
    return angle

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


    def update(self,surface,keys):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse = pygame.mouse.get_pressed()
        tips = setup.GRAPHICS['tips.png']
        self.setup_background()
        surface.blit(self.background, self.viewport)
        LoadScreen.angle = wrap_angle(LoadScreen.angle - 1)
        rtips=pygame.transform.rotate(tips, abs(math.sin(math.radians(LoadScreen.angle))*10))
        print(pygame.mouse.get_pos())
        if 209 < mouse_x < 289 and 313 < mouse_y < 519:
            if mouse == (0, 0, 0):
                surface.blit(rtips, (208, 295))
                surface.blit(tips, (843 - 42, 300))
                surface.blit(tips, (565 - 42, 337))
                pygame.display.update()
            elif mouse == (1, 0, 0):
                self.finished=True
        else:
            surface.blit(tips, (843-42, 300))
            surface.blit(tips, (565-42, 337))
            surface.blit(tips, (208, 295))



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