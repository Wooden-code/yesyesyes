import pygame
from .. import setup  # ..是上一级文件
from .. import tools
from .. import constants as C
from ..components import info  # 到上一级目录平行的components
import random



class Body_title:
    instance = None
    flag=False
    def __init__(self):
        game_info = {
            'score': 0,
            'coin': 0,
            'lives': 3,
            'player_state': 'small'  # 大的还是小的什么的

        }
        self.start(game_info)
    def start(self,game_info):
        self.background=[setup.GRAPHICS['next_3.png'],setup.GRAPHICS['next_3.png'],setup.GRAPHICS['body_title_chibifu.png']]
        self.index=0
        self.background_rect = self.background[self.index].get_rect()
        self.game_ground = pygame.Surface((self.background_rect.width, self.background_rect.height))

        self.background[2]= pygame.transform.scale(self.background[2], (
            int(self.background_rect.width * 1), int(self.background_rect.height *1)))
        self.game_info=game_info
        self.time=pygame.time.get_ticks()

        self.finished=False
        self.next='load_screen'
    def update(self,surface,keys):

        surface.blit(self.background[0], (0,0))
        #self.background_image=self.background[self.index]
        mouse=pygame.mouse.get_pressed()
        if mouse==(1,0,0):
                if self.index<len(self.background)-1:
                    self.index+=1
                    pygame.time.wait(550)
                    self.background[0].blit(self.background[self.index], (0, 0))
                else:
                    pygame.time.wait(500)
                    self.finished=True
                    self.next='load_screen'
