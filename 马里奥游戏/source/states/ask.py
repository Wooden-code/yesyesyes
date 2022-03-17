import pygame
from .. import setup  # ..是上一级文件
from .. import tools
from .. import constants as C
from ..components import info  # 到上一级目录平行的components
import random



class Ask:
    instance = None
    expanded_i = 1
    def __init__(self):
        game_info={
            'score':0,
            'coin':0,
            'lives':3,
            'player_state':'small'#大的还是小的什么的

        }
        self.start(game_info)

    def start(self,game_info):
            self.game_info=game_info

            self.setup_background()
            self.ask1 = setup.GRAPHICS['paint_1.png']
            self.ask2 = setup.GRAPHICS['paint_2.png']
            self.ask3 = setup.GRAPHICS['paint_3.png']
            self.ask4 = setup.GRAPHICS['paint_4.png']
            self.ask5 = setup.GRAPHICS['paint_5.png']
           # self.ask6 = setup.GRAPHICS['ask_6.png']
            self.frames=[self.ask5,self.ask4,self.ask3,self.ask2,self.ask1]

            self.ask()
            self.finished = False  # 只要这个阶段还在运行就不完结
            self.next='load_screen'







    def setup_background(self):  # 设置底图\\

        self.background = setup.GRAPHICS['words.png']
        self.background_rect = self.background.get_rect()
        self.background = pygame.transform.scale(self.background, (
            int(self.background_rect.width * C.BG_W_MULTI), int(self.background_rect.height * C.BG_H_MULTI)))
        self.viewport = setup.SCREEN.get_rect()  # 滑动窗口
        self.game_ground=pygame.Surface((self.background_rect.width,self.background_rect.height))







    def update(self, surface, keys):  # 更新操作
        surface.blit(self.background,self.background_rect)
        check_right= tools.button(0, 0, 100, 100)

        if check_right==8:
            self.finished=True
            self.next = 'level'
            print('yes')
        elif check_right==6:
            self.finished=True

            self.next = 'main_menu'



    def ask(self):
        self.image=self.frames[random.randint(0,4)]

    def draw(self,surface):
        self.game_ground.blit(self.background,(0,0))




