import pygame
from .. import setup  # ..是上一级文件
from .. import tools
from .. import constants as C
from ..components import info  # 到上一级目录平行的components
import random



class Chuangguan:
    instance = None
    flag=False
    tt=0
    def __init__(self):
        game_info = {
            'score': 0,
            'coin': 0,
            'lives': 3,
            'player_state': 'small'  # 大的还是小的什么的

        }
        self.start(game_info)
    def start(self,game_info):
        self.background=[setup.GRAPHICS['chuangguan_1.png'],setup.GRAPHICS['chuangguan_1.png'],setup.GRAPHICS['chuangguan_2.png'],setup.GRAPHICS['chuangguan_3.png'],setup.GRAPHICS['chuangguan_4.png'],setup.GRAPHICS['chuangguan_5.png'],
                         setup.GRAPHICS['chuangguan_5.png'],setup.GRAPHICS['chuangguan_6.png'],setup.GRAPHICS['chuangguan_7.png'],setup.GRAPHICS['chuangguan_8.png'],setup.GRAPHICS['chuangguan_9.png'],setup.GRAPHICS['chuangguan_12.png'],setup.GRAPHICS['chuangguan_3.png'],
                         setup.GRAPHICS['chuangguan_4.png'],setup.GRAPHICS['chuangguan_10.png'],setup.GRAPHICS['chuangguan_10.png'],setup.GRAPHICS['chuangguan_11.png'],setup.GRAPHICS['chuangguan_end1.png'],setup.GRAPHICS['chuangguan_end3.png']]
        if self.tt==0:
            self.index=0
        elif self.tt==1:
            self.index=5
        elif self.tt==2:
            self.index=14
        self.background_rect = self.background[self.index].get_rect()
        self.game_ground = pygame.Surface((self.background_rect.width, self.background_rect.height))
       # self.background[self.index]= pygame.transform.scale(self.background[self.index], (
            #int(self.background_rect.width * 0.46), int(self.background_rect.height *0.57)))
        self.game_info=game_info
        self.time=pygame.time.get_ticks()

        self.finished=False
        self.next='load_screen'
    def update(self,surface,keys):

        surface.blit(self.background[0], (0,0))
        #self.background_image=self.background[self.index]
        mouse=pygame.mouse.get_pressed()
        if mouse==(1,0,0):
                if self.index<4:
                    self.index+=1
                    pygame.time.wait(550)
                    self.background[0].blit(self.background[self.index], (0, 0))
                elif self.index==4:
                    self.tt=1
                    pygame.time.wait(500)
                    self.finished=True
                    self.next='drop'
                elif self.index>4 and self.index<13:
                    self.index += 1
                    pygame.time.wait(550)
                    self.background[0].blit(self.background[self.index], (0, 0))
                elif self.index==13:
                    self.tt = 2
                    pygame.time.wait(500)
                    self.finished = True
                    self.next = 'chengyu'
                elif self.index>13 and self.index<18:
                    self.index += 1
                    pygame.time.wait(550)
                    self.background[0].blit(self.background[self.index], (0, 0))
                elif self.index==18:
                    print('aaaaaaaaaaaaa')
                    self.tt = 3
                    pygame.time.wait(500)
                    self.finished = True
                    self.next = 'body_title'




