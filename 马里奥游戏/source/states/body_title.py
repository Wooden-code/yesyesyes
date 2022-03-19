import pygame
from .. import setup  # ..是上一级文件
from .. import tools
from .. import constants as C
from ..components import info  # 到上一级目录平行的components
import random



class Body_title:
    instance = None
    def __init__(self):
        game_info = {
            'score': 0,
            'coin': 0,
            'lives': 3,
            'player_state': 'small'  # 大的还是小的什么的

        }
        self.start(game_info)
    def start(self,game_info):
        self.background=setup.GRAPHICS['body_title_chibifu.png']
        self.background_rect = self.background.get_rect()
        self.game_ground = pygame.Surface((self.background_rect.width, self.background_rect.height))
        self.background = pygame.transform.scale(self.background, (
            int(self.background_rect.width * 0.46), int(self.background_rect.height *0.57)))
        self.game_info=game_info
        self.time=pygame.time.get_ticks()

        self.finished=False
        self.next='load_screen'
    def update(self,surface,keys):
        surface.blit(self.background, self.background_rect)

        if keys[pygame.K_RETURN]:
                self.finished=True
                self.next='load_screen'
