
import pygame.sprite
from .. import tools,setup
from .. import constants as C
from ..states import level


class FlashingCoin(pygame.sprite.Sprite):#引入这个精灵方法
    def __init__(self):#类的初始化 初始化一些变量
        pygame.sprite.Sprite.__init__(self)
        pass


    def load_frames(self,frame_rects):
        pass
    def update(self):
        pass

class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y, type,group, name='coin'):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.type = type
        self.group=group
        self.name = name



        if self.group==0:
            if self.type < 16:
                try:
                    self.image=setup.GRAPHICS[f'sentence{self.type+1}.png']
                except:
                    self.image = setup.GRAPHICS[f'sentence_{self.type + 1}.png']
            else:
                self.image = setup.GRAPHICS[f'pronounce_{self.type-15}.png']


        elif self.group==1:
            self.image=setup.GRAPHICS[f'ji_{self.type+1}.png']

        elif self.group==2:
            self.image=setup.GRAPHICS[f'han_{self.type+1}.png']
        elif self.group==3:
            self.image = setup.GRAPHICS[f'you_{self.type+1}.png']
        elif self.group==4:#回血
            self.image=setup.GRAPHICS[f're_blood_{self.type}.png']

        elif self.group==5:
            self.image=setup.GRAPHICS['sentence_close.png']


        self.rect = self.image.get_rect()

        self.rect.x = self.x
        self.rect.y = self.y
        self.gravity = C.GRAVITY

        self.state = 'rest'  # 默认状态
        self.timer = 0
    def check_y(self):
        pass


    def update(self):
        self.current_time = pygame.time.get_ticks()
        self.handle_states()

    def handle_states(self):
        if self.state == 'rest':
            self.rest()
    def rest(self):
        pass