import pygame
from .. import setup  # ..是上一级文件
from .. import tools
from .. import constants as C
from ..components import info  # 到上一级目录平行的components
import random
import os


class drop:
    drop1,drop2,drop3,drop4,drop5,drop6,drop7,drop8,drop9,drop10=[752,701],[440,758],[596,701],[440,701],[674,701],[752,758],[596,758],[518,701],[674,758],[518,758]

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
        self.qin_1 = setup.GRAPHICS['qin_1.png']
        self.qin_2 = setup.GRAPHICS['qin_2.png']
        self.kan_1 = setup.GRAPHICS['kan_1.png']
        self.kan_2 = setup.GRAPHICS['kan_2.png']
        self.shi_1 = setup.GRAPHICS['shi_1.png']
        self.shi_2 = setup.GRAPHICS['shi_2.png']
        self.shou_1 = setup.GRAPHICS['shou_1.png']
        self.shou_2 = setup.GRAPHICS['shou_2.png']
        self.yi_1 = setup.GRAPHICS['yi_1.png']
        self.yi_2 = setup.GRAPHICS['yi_2.png']

        self.setup_background()

        self.finished = False  # 只要这个阶段还在运行就不完结
        self.next = 'body_title'

    def setup_background(self):  # 设置底图
        self.num = random.randint(0, 2)
        self.background = setup.GRAPHICS['game_2_background.png']
        self.background_rect = self.background.get_rect()
        self.game_ground = pygame.Surface((self.background_rect.width, self.background_rect.height))

    def update(self, surface, flag):  # 拖拽操作
        print(pygame.mouse.get_pos())
        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse = pygame.mouse.get_pressed()
        surface.blit(self.background, (0,0))
        surface.blit(self.qin_1, (drop.drop1[0]-25, drop.drop1[1]-25))
        surface.blit(self.qin_2, (drop.drop2[0]-25, drop.drop2[1]-25))
        surface.blit(self.kan_1, (drop.drop3[0]-25, drop.drop3[1]-25))
        surface.blit(self.kan_2, (drop.drop4[0]-25, drop.drop4[1]-25))
        surface.blit(self.shi_1, (drop.drop5[0]-25, drop.drop5[1]-25))
        surface.blit(self.shi_2, (drop.drop6[0]-25, drop.drop6[1]-25))
        surface.blit(self.shou_1, (drop.drop7[0] - 25, drop.drop7[1] - 25))
        surface.blit(self.shou_2, (drop.drop8[0] - 25, drop.drop8[1] - 25))
        surface.blit(self.yi_1, (drop.drop9[0] - 25, drop.drop9[1] - 25))
        surface.blit(self.yi_2, (drop.drop10[0] - 25, drop.drop10[1] - 25))
        if drop.drop1[0]-25<mouse_x<drop.drop1[0]+25 and drop.drop1[1]-25<mouse_y<drop.drop1[1]+25 and mouse==(1,0,0):
            surface.blit(self.background, (0,0))
            surface.blit(self.qin_1, (drop.drop1[0] - 25, drop.drop1[1] - 25))
            surface.blit(self.qin_2, (drop.drop2[0] - 25, drop.drop2[1] - 25))
            surface.blit(self.kan_1, (drop.drop3[0] - 25, drop.drop3[1] - 25))
            surface.blit(self.kan_2, (drop.drop4[0] - 25, drop.drop4[1] - 25))
            surface.blit(self.shi_1, (drop.drop5[0] - 25, drop.drop5[1] - 25))
            surface.blit(self.shi_2, (drop.drop6[0] - 25, drop.drop6[1] - 25))
            surface.blit(self.shou_1, (drop.drop7[0] - 25, drop.drop7[1] - 25))
            surface.blit(self.shou_2, (drop.drop8[0] - 25, drop.drop8[1] - 25))
            surface.blit(self.yi_1, (drop.drop9[0] - 25, drop.drop9[1] - 25))
            surface.blit(self.yi_2, (drop.drop10[0] - 25, drop.drop10[1] - 25))

            drop.drop1[0], drop.drop1[1] = mouse_x, mouse_y

        if drop.drop2[0]-25<mouse_x<drop.drop2[0]+25 and drop.drop2[1]-25<mouse_y<drop.drop2[1]+25 and mouse==(1,0,0):
            surface.blit(self.background, (0,0))
            surface.blit(self.qin_1, (drop.drop1[0] - 25, drop.drop1[1] - 25))
            surface.blit(self.qin_2, (drop.drop2[0] - 25, drop.drop2[1] - 25))
            surface.blit(self.kan_1, (drop.drop3[0] - 25, drop.drop3[1] - 25))
            surface.blit(self.kan_2, (drop.drop4[0] - 25, drop.drop4[1] - 25))
            surface.blit(self.shi_1, (drop.drop5[0] - 25, drop.drop5[1] - 25))
            surface.blit(self.shi_2, (drop.drop6[0] - 25, drop.drop6[1] - 25))
            surface.blit(self.shou_1, (drop.drop7[0] - 25, drop.drop7[1] - 25))
            surface.blit(self.shou_2, (drop.drop8[0] - 25, drop.drop8[1] - 25))
            surface.blit(self.yi_1, (drop.drop9[0] - 25, drop.drop9[1] - 25))
            surface.blit(self.yi_2, (drop.drop10[0] - 25, drop.drop10[1] - 25))

            drop.drop2[0],drop.drop2[1]=mouse_x, mouse_y

        elif (drop.drop3[0]-25<mouse_x<drop.drop3[0]+25 and drop.drop3[1]-25<mouse_y<drop.drop3[1]+25 and mouse==(1,0,0)) or(drop.drop4[0]-25<mouse_x<drop.drop4[0]+25 and drop.drop4[1]-25<mouse_y<drop.drop4[1]+25 and mouse==(1,0,0)):
            if drop.drop3[0]-25<mouse_x<drop.drop3[0]+25 and drop.drop3[1]-25<mouse_y<drop.drop3[1]+25 and mouse==(1,0,0):
                surface.blit(self.background, (0,0))
                surface.blit(self.qin_1, (drop.drop1[0] - 25, drop.drop1[1] - 25))
                surface.blit(self.qin_2, (drop.drop2[0] - 25, drop.drop2[1] - 25))
                surface.blit(self.kan_1, (drop.drop3[0] - 25, drop.drop3[1] - 25))
                surface.blit(self.kan_2, (drop.drop4[0] - 25, drop.drop4[1] - 25))
                surface.blit(self.shi_1, (drop.drop5[0] - 25, drop.drop5[1] - 25))
                surface.blit(self.shi_2, (drop.drop6[0] - 25, drop.drop6[1] - 25))
                surface.blit(self.shou_1, (drop.drop7[0] - 25, drop.drop7[1] - 25))
                surface.blit(self.shou_2, (drop.drop8[0] - 25, drop.drop8[1] - 25))
                surface.blit(self.yi_1, (drop.drop9[0] - 25, drop.drop9[1] - 25))
                surface.blit(self.yi_2, (drop.drop10[0] - 25, drop.drop10[1] - 25))

                drop.drop3[0],drop.drop3[1]=mouse_x, mouse_y

            if drop.drop4[0]-25<mouse_x<drop.drop4[0]+25 and drop.drop4[1]-25<mouse_y<drop.drop4[1]+25 and mouse==(1,0,0):
                surface.blit(self.background, (0,0))
                surface.blit(self.qin_1, (drop.drop1[0] - 25, drop.drop1[1] - 25))
                surface.blit(self.qin_2, (drop.drop2[0] - 25, drop.drop2[1] - 25))
                surface.blit(self.kan_1, (drop.drop3[0] - 25, drop.drop3[1] - 25))
                surface.blit(self.kan_2, (drop.drop4[0] - 25, drop.drop4[1] - 25))
                surface.blit(self.shi_1, (drop.drop5[0] - 25, drop.drop5[1] - 25))
                surface.blit(self.shi_2, (drop.drop6[0] - 25, drop.drop6[1] - 25))
                surface.blit(self.shou_1, (drop.drop7[0] - 25, drop.drop7[1] - 25))
                surface.blit(self.shou_2, (drop.drop8[0] - 25, drop.drop8[1] - 25))
                surface.blit(self.yi_1, (drop.drop9[0] - 25, drop.drop9[1] - 25))
                surface.blit(self.yi_2, (drop.drop10[0] - 25, drop.drop10[1] - 25))

                drop.drop4[0],drop.drop4[1]=mouse_x, mouse_y

        elif (drop.drop5[0]-25<mouse_x<drop.drop5[0]+25 and drop.drop5[1]-25<mouse_y<drop.drop5[1]+25and mouse==(1,0,0))or(drop.drop6[0]-25<mouse_x<drop.drop6[0]+25 and drop.drop6[1]-25<mouse_y<drop.drop6[1]+25 and mouse==(1,0,0)):
            if drop.drop5[0]-25<mouse_x<drop.drop5[0]+25 and drop.drop5[1]-25<mouse_y<drop.drop5[1]+25and mouse==(1,0,0):
                surface.blit(self.background, (0,0))
                surface.blit(self.qin_1, (drop.drop1[0] - 25, drop.drop1[1] - 25))
                surface.blit(self.qin_2, (drop.drop2[0] - 25, drop.drop2[1] - 25))
                surface.blit(self.kan_1, (drop.drop3[0] - 25, drop.drop3[1] - 25))
                surface.blit(self.kan_2, (drop.drop4[0] - 25, drop.drop4[1] - 25))
                surface.blit(self.shi_1, (drop.drop5[0] - 25, drop.drop5[1] - 25))
                surface.blit(self.shi_2, (drop.drop6[0] - 25, drop.drop6[1] - 25))
                surface.blit(self.shou_1, (drop.drop7[0] - 25, drop.drop7[1] - 25))
                surface.blit(self.shou_2, (drop.drop8[0] - 25, drop.drop8[1] - 25))
                surface.blit(self.yi_1, (drop.drop9[0] - 25, drop.drop9[1] - 25))
                surface.blit(self.yi_2, (drop.drop10[0] - 25, drop.drop10[1] - 25))

                drop.drop5[0],drop.drop5[1]=mouse_x, mouse_y

            if drop.drop6[0]-25<mouse_x<drop.drop6[0]+25 and drop.drop6[1]-25<mouse_y<drop.drop6[1]+25 and mouse==(1,0,0):
                surface.blit(self.background, (0,0))
                surface.blit(self.qin_1, (drop.drop1[0] - 25, drop.drop1[1] - 25))
                surface.blit(self.qin_2, (drop.drop2[0] - 25, drop.drop2[1] - 25))
                surface.blit(self.kan_1, (drop.drop3[0] - 25, drop.drop3[1] - 25))
                surface.blit(self.kan_2, (drop.drop4[0] - 25, drop.drop4[1] - 25))
                surface.blit(self.shi_1, (drop.drop5[0] - 25, drop.drop5[1] - 25))
                surface.blit(self.shi_2, (drop.drop6[0] - 25, drop.drop6[1] - 25))
                surface.blit(self.shou_1, (drop.drop7[0] - 25, drop.drop7[1] - 25))
                surface.blit(self.shou_2, (drop.drop8[0] - 25, drop.drop8[1] - 25))
                surface.blit(self.yi_1, (drop.drop9[0] - 25, drop.drop9[1] - 25))
                surface.blit(self.yi_2, (drop.drop10[0] - 25, drop.drop10[1] - 25))
                drop.drop6[0],drop.drop6[1]=mouse_x, mouse_y

        elif (drop.drop7[0] -25 < mouse_x < drop.drop7[0] + 25 and drop.drop7[1] - 25 < mouse_y < drop.drop7[1] +25 and mouse == (1, 0, 0))or(drop.drop8[0] - 25 < mouse_x < drop.drop8[0] + 25 and drop.drop8[1] - 25 < mouse_y < drop.drop8[1] + 25 and mouse == (1, 0, 0)):
            if drop.drop7[0] -25 < mouse_x < drop.drop7[0] + 25 and drop.drop7[1] - 25 < mouse_y < drop.drop7[1] +25 and mouse == (1, 0, 0):
                surface.blit(self.background, (0, 0))
                surface.blit(self.qin_1, (drop.drop1[0] - 25, drop.drop1[1] - 25))
                surface.blit(self.qin_2, (drop.drop2[0] - 25, drop.drop2[1] - 25))
                surface.blit(self.kan_1, (drop.drop3[0] - 25, drop.drop3[1] - 25))
                surface.blit(self.kan_2, (drop.drop4[0] - 25, drop.drop4[1] - 25))
                surface.blit(self.shi_1, (drop.drop5[0] - 25, drop.drop5[1] - 25))
                surface.blit(self.shi_2, (drop.drop6[0] - 25, drop.drop6[1] - 25))
                surface.blit(self.shou_1, (drop.drop7[0] - 25, drop.drop7[1] - 25))
                surface.blit(self.shou_2, (drop.drop8[0] - 25, drop.drop8[1] - 25))
                surface.blit(self.yi_1, (drop.drop9[0] - 25, drop.drop9[1] - 25))
                surface.blit(self.yi_2, (drop.drop10[0] - 25, drop.drop10[1] - 25))

                drop.drop7[0], drop.drop7[1] = mouse_x, mouse_y

            if drop.drop8[0] - 25 < mouse_x < drop.drop8[0] + 25 and drop.drop8[1] - 25 < mouse_y < drop.drop8[1] + 25 and mouse == (1, 0, 0):
                surface.blit(self.background, (0, 0))
                surface.blit(self.qin_1, (drop.drop1[0] - 25, drop.drop1[1] - 25))
                surface.blit(self.qin_2, (drop.drop2[0] - 25, drop.drop2[1] - 25))
                surface.blit(self.kan_1, (drop.drop3[0] - 25, drop.drop3[1] - 25))
                surface.blit(self.kan_2, (drop.drop4[0] - 25, drop.drop4[1] - 25))
                surface.blit(self.shi_1, (drop.drop5[0] - 25, drop.drop5[1] - 25))
                surface.blit(self.shi_2, (drop.drop6[0] - 25, drop.drop6[1] - 25))
                surface.blit(self.shou_1, (drop.drop7[0] - 25, drop.drop7[1] - 25))
                surface.blit(self.shou_2, (drop.drop8[0] - 25, drop.drop8[1] - 25))
                surface.blit(self.yi_1, (drop.drop9[0] - 25, drop.drop9[1] - 25))
                surface.blit(self.yi_2, (drop.drop10[0] - 25, drop.drop10[1] - 25))

                drop.drop8[0], drop.drop8[1] = mouse_x, mouse_y

        elif (drop.drop9[0] - 25 < mouse_x < drop.drop9[0] + 25 and drop.drop9[1] - 25 < mouse_y < drop.drop9[
            1] + 25 and mouse == (1, 0, 0))or(drop.drop10[0] - 25 < mouse_x < drop.drop10[0] + 25 and drop.drop10[1] - 25 < mouse_y < drop.drop10[
                1] + 25 and mouse == (1, 0, 0)):
            if drop.drop9[0] - 25 < mouse_x < drop.drop9[0] + 25 and drop.drop9[1] - 25 < mouse_y < drop.drop9[
            1] + 25 and mouse == (1, 0, 0):
                surface.blit(self.background, (0, 0))
                surface.blit(self.qin_1, (drop.drop1[0] - 25, drop.drop1[1] - 25))
                surface.blit(self.qin_2, (drop.drop2[0] - 25, drop.drop2[1] - 25))
                surface.blit(self.kan_1, (drop.drop3[0] - 25, drop.drop3[1] - 25))
                surface.blit(self.kan_2, (drop.drop4[0] - 25, drop.drop4[1] - 25))
                surface.blit(self.shi_1, (drop.drop5[0] - 25, drop.drop5[1] - 25))
                surface.blit(self.shi_2, (drop.drop6[0] - 25, drop.drop6[1] - 25))
                surface.blit(self.shou_1, (drop.drop7[0] - 25, drop.drop7[1] - 25))
                surface.blit(self.shou_2, (drop.drop8[0] - 25, drop.drop8[1] - 25))
                surface.blit(self.yi_1, (drop.drop9[0] - 25, drop.drop9[1] - 25))
                surface.blit(self.yi_2, (drop.drop10[0] - 25, drop.drop10[1] - 25))

                drop.drop9[0], drop.drop9[1] = mouse_x, mouse_y

            if drop.drop10[0] - 25 < mouse_x < drop.drop10[0] + 25 and drop.drop10[1] - 25 < mouse_y < drop.drop10[
                1] + 25 and mouse == (1, 0, 0):
                surface.blit(self.background, (0, 0))
                surface.blit(self.qin_1, (drop.drop1[0] - 25, drop.drop1[1] - 25))
                surface.blit(self.qin_2, (drop.drop2[0] - 25, drop.drop2[1] - 25))
                surface.blit(self.kan_1, (drop.drop3[0] - 25, drop.drop3[1] - 25))
                surface.blit(self.kan_2, (drop.drop4[0] - 25, drop.drop4[1] - 25))
                surface.blit(self.shi_1, (drop.drop5[0] - 25, drop.drop5[1] - 25))
                surface.blit(self.shi_2, (drop.drop6[0] - 25, drop.drop6[1] - 25))
                surface.blit(self.shou_1, (drop.drop7[0] - 25, drop.drop7[1] - 25))
                surface.blit(self.shou_2, (drop.drop8[0] - 25, drop.drop8[1] - 25))
                surface.blit(self.yi_1, (drop.drop9[0] - 25, drop.drop9[1] - 25))
                surface.blit(self.yi_2, (drop.drop10[0] - 25, drop.drop10[1] - 25))

                drop.drop10[0], drop.drop10[1] = mouse_x, mouse_y



        if 647 < drop.drop1[0] <647+51 and 215 < drop.drop1[1] < 215+51 and mouse == (0, 0, 0):
            if  647 < drop.drop3[0] <647+51 and 512 < drop.drop3[1] < 512+51 :
                if 531 < drop.drop5[0] < 531 + 51 and 215< drop.drop5[1] < 215+51:
                    if 531 < drop.drop7[0] < 531 + 51 and 272< drop.drop7[1] < 272+51:
                        if 531 < drop.drop9[0] < 531 + 51 and 608 < drop.drop9[1] < 608+51:
                            self.finished=True