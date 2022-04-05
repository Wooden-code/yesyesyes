import pygame
from .. import setup  # ..是上一级文件
from .. import tools
from .. import constants as C
from ..components import info  # 到上一级目录平行的components
import random
import os


class drop:
    drop1,drop2,drop3,drop4,drop5,drop6=[760,228],[597,380],[420,228],[597,228],[420,380],[760,380]

    def __init__(self):
        game_info = {
            'score': 0,
            'coin': 0,
            'num': 0,
            'player_state': 'small'  # 大的还是小的什么的

        }
        self.start(game_info)

    def start(self, game_info):
        self.game_info = game_info
        self.you_1 = setup.GRAPHICS['you_1.png']
        self.you_2 = setup.GRAPHICS['you_2.png']
        self.you_3 = setup.GRAPHICS['you_3.png']
        self.you_4 = setup.GRAPHICS['you_4.png']
        self.you_5 = setup.GRAPHICS['you_5.png']
        self.you_6 = setup.GRAPHICS['you_6.png']

        self.setup_background()

        self.finished = False  # 只要这个阶段还在运行就不完结
        self.next = 'chuangguan'

    def setup_background(self):  # 设置底图
        self.num = random.randint(0, 2)
        self.background = setup.GRAPHICS['game_1_background.png']
        self.background_rect = self.background.get_rect()
        self.game_ground = pygame.Surface((self.background_rect.width, self.background_rect.height))

    def update(self, surface, flag):  # 拖拽操作
        print(pygame.mouse.get_pos())
        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse = pygame.mouse.get_pressed()
        surface.blit(self.background, (0,0))
        surface.blit(self.you_1, (drop.drop1[0]-34, drop.drop1[1]-50))
        surface.blit(self.you_2, (drop.drop2[0]-34, drop.drop2[1]-50))
        surface.blit(self.you_3, (drop.drop3[0]-34, drop.drop3[1]-50))
        surface.blit(self.you_4, (drop.drop4[0]-34, drop.drop4[1]-50))
        surface.blit(self.you_5, (drop.drop5[0]-34, drop.drop5[1]-50))
        surface.blit(self.you_6, (drop.drop6[0]-34, drop.drop6[1]-50))
        if drop.drop1[0]-50<mouse_x<drop.drop1[0]+70 and drop.drop1[1]-50<mouse_y<drop.drop1[1]+100 and mouse==(1,0,0):
            surface.blit(self.background, (0,0))
            surface.blit(self.you_2, (drop.drop2[0]-34, drop.drop2[1]-50))
            surface.blit(self.you_3, (drop.drop3[0]-34, drop.drop3[1]-50))
            surface.blit(self.you_4, (drop.drop4[0]-34, drop.drop4[1]-50))
            surface.blit(self.you_5, (drop.drop5[0]-34, drop.drop5[1]-50))
            surface.blit(self.you_6, (drop.drop6[0]-34, drop.drop6[1]-50))

            surface.blit(self.you_1, (drop.drop1[0]-34,drop.drop1[1]-50))

            drop.drop1[0],drop.drop1[1]=mouse_x, mouse_y

        elif drop.drop2[0]-50<mouse_x<drop.drop2[0]+70 and drop.drop2[1]-50<mouse_y<drop.drop2[1]+100 and mouse==(1,0,0):
            surface.blit(self.background, (0,0))
            surface.blit(self.you_1, (drop.drop1[0]-34, drop.drop1[1]-50))
            surface.blit(self.you_3, (drop.drop3[0]-34, drop.drop3[1]-50))
            surface.blit(self.you_4, (drop.drop4[0]-34, drop.drop4[1]-50))
            surface.blit(self.you_5, (drop.drop5[0]-34, drop.drop5[1]-50))
            surface.blit(self.you_6, (drop.drop6[0]-34, drop.drop6[1]-50))

            surface.blit(self.you_2, (drop.drop2[0]-34,drop.drop2[1]-50))

            drop.drop2[0],drop.drop2[1]=mouse_x, mouse_y

        elif drop.drop3[0]-50<mouse_x<drop.drop3[0]+70 and drop.drop3[1]-50<mouse_y<drop.drop3[1]+100 and mouse==(1,0,0):
            surface.blit(self.background, (0,0))
            surface.blit(self.you_2, (drop.drop2[0]-34, drop.drop2[1]-50))
            surface.blit(self.you_1, (drop.drop1[0]-34, drop.drop1[1]-50))
            surface.blit(self.you_4, (drop.drop4[0]-34, drop.drop4[1]-50))
            surface.blit(self.you_5, (drop.drop5[0]-34, drop.drop5[1]-50))
            surface.blit(self.you_6, (drop.drop6[0]-34, drop.drop6[1]-50))

            surface.blit(self.you_3, (drop.drop3[0]-34,drop.drop3[1]-50))

            drop.drop3[0],drop.drop3[1]=mouse_x, mouse_y

        elif drop.drop4[0]-50<mouse_x<drop.drop4[0]+70 and drop.drop4[1]-50<mouse_y<drop.drop4[1]+100 and mouse==(1,0,0):
            surface.blit(self.background, (0,0))
            surface.blit(self.you_2, (drop.drop2[0]-34, drop.drop2[1]-50))
            surface.blit(self.you_3, (drop.drop3[0]-34, drop.drop3[1]-50))
            surface.blit(self.you_1, (drop.drop1[0]-34, drop.drop1[1]-50))
            surface.blit(self.you_5, (drop.drop5[0]-34, drop.drop5[1]-50))
            surface.blit(self.you_6, (drop.drop6[0]-34, drop.drop6[1]-50))

            surface.blit(self.you_4, (drop.drop4[0]-34,drop.drop4[1]-50))

            drop.drop4[0],drop.drop4[1]=mouse_x, mouse_y

        elif drop.drop5[0]-50<mouse_x<drop.drop5[0]+70 and drop.drop5[1]-50<mouse_y<drop.drop5[1]+100 and mouse==(1,0,0):
            surface.blit(self.background, (0,0))
            surface.blit(self.you_2, (drop.drop2[0]-34, drop.drop2[1]-50))
            surface.blit(self.you_3, (drop.drop3[0]-34, drop.drop3[1]-50))
            surface.blit(self.you_4, (drop.drop4[0]-34, drop.drop4[1]-50))
            surface.blit(self.you_1, (drop.drop1[0]-34, drop.drop1[1]-50))
            surface.blit(self.you_6, (drop.drop6[0]-34, drop.drop6[1]-50))

            surface.blit(self.you_5, (drop.drop5[0]-34,drop.drop5[1]-50))

            drop.drop5[0],drop.drop5[1]=mouse_x, mouse_y

        elif drop.drop6[0]-50<mouse_x<drop.drop6[0]+70 and drop.drop6[1]-50<mouse_y<drop.drop6[1]+100 and mouse==(1,0,0):
            surface.blit(self.background, (0,0))
            surface.blit(self.you_2, (drop.drop2[0]-34, drop.drop2[1]-50))
            surface.blit(self.you_3, (drop.drop3[0]-34, drop.drop3[1]-50))
            surface.blit(self.you_4, (drop.drop4[0]-34, drop.drop4[1]-50))
            surface.blit(self.you_5, (drop.drop5[0]-34, drop.drop5[1]-50))
            surface.blit(self.you_1, (drop.drop1[0]-34, drop.drop1[1]-50))

            surface.blit(self.you_6, (drop.drop6[0]-34,drop.drop6[1]-50))

            drop.drop6[0],drop.drop6[1]=mouse_x, mouse_y



        if 280 < drop.drop1[0] <280+108 and 500 < drop.drop1[1] < 500+108 and mouse == (0, 0, 0):
            if 407 < drop.drop2[0] <407+108 and 500 < drop.drop2[1] < 500+108 :
                if 534 < drop.drop3[0] < 534 + 108 and 500 < drop.drop3[1] < 500 + 108:
                    if 659 < drop.drop4[0] < 659 + 108 and 500 < drop.drop4[1] < 500 + 108:
                        if 788 < drop.drop5[0] < 788 + 108 and 500 < drop.drop5[1] < 500 + 108:
                            if 912 < drop.drop6[0] < 912 + 108 and 500 < drop.drop6[1] < 500 + 108:
                                pygame.mixer.Sound(os.path.abspath("resource/music/eat.ogg")).play()
                                self.finished=True