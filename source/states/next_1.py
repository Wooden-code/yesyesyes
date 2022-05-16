import pygame
from .. import setup  # ..是上一级文件
from .. import tools
from .. import constants as C
from ..components import info  # 到上一级目录平行的components
import random



class Next_1:
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
        self.background=setup.GRAPHICS['next_1.png']
        self.index=0
        self.background_rect=self.background.get_rect()
        self.game_ground = pygame.Surface((self.background_rect.width, self.background_rect.height))

        self.game_info=game_info
        self.time=pygame.time.get_ticks()

        self.finished=False
        self.next='level2'
        if self.flag==False:
            self.flag=True
            self.time=pygame.time.get_ticks()
    def update(self,surface,keys):
        surface.blit(self.background, (0, 0))
        print('iiii')
        if pygame.time.get_ticks()-self.time>3000:
            self.finished=True


