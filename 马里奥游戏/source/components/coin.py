
import pygame.sprite
from .. import tools,setup
from .. import constants as C
from ..states import level


class FlashingCoin(pygame.sprite.Sprite):#引入这个精灵方法
    def __init__(self):#类的初始化 初始化一些变量
        pygame.sprite.Sprite.__init__(self)
        self.frames=[]
        self.frame_index=0
        frame_rects=[(1,160,5,8),(9,160,5,8),(17,160,5,8),(9,160,5,8)]#列表内放四个元组，每个元组是金币图片的位置，分别记录x，y，宽，高
        self.load_frames(frame_rects)
        self.image=self.frames[self.frame_index]#第一帧
        self.rect=self.image.get_rect()#指定皮肤
        self.rect.x=280#想让金币放置的位置
        self.rect.y=58
        self.timer=0


    def load_frames(self,frame_rects):
        sheet=setup.GRAPHICS['item_objects.png']
        for frame_rect in frame_rects:
            self.frames.append(tools.get_image(sheet,*frame_rect,(0,0,0),C.BG_W_MULTI))# *frame_rect是一个解包，将上面这个列表放入这里面时自动变成四个变量

    def update(self):
        self.current_time=pygame.time.get_ticks()#获取当前时间
        frame_durations=[375,125,125,125]#第一个变换间隔久一点
        # self.timer = self.current_time

        if self.timer==0:
            self.timer=self.current_time
        elif self.current_time - self.timer > frame_durations[self.frame_index]:
            self.frame_index += 1
            self.frame_index %= 4# 4为1循环
            self.timer = self.current_time

        self.image = self.frames[self.frame_index]

class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y, coin_type, group, name='coin'):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.coin_type = coin_type
        self.group = group
        self.name = name

        self.frame_rects =[(1,160,5,8),(9,160,5,8),(17,160,5,8),(9,160,5,8)]

        self.frames = []
        for frame_rect in self.frame_rects:
            self.frames.append(tools.get_image(setup.GRAPHICS['words.png'], *frame_rect, (0, 0, 0), C.BRICK_MULTI))

        self.frame_index = 0
        self.image = self.frames[self.frame_index]
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