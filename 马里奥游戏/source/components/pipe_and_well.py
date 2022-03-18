import pygame
from .. import tools,setup
from .. import constants as C

class Pipe_and_well(pygame.sprite.Sprite):
    def __init__(self, x, y, type, group, name='pipe'):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.type = type
        self.group = group
        self.name = name
        self.pipe_frame_rects =(242.7,235.5,340,358.7)
        self.well_frame_rects = (242.7, 235.5, 340, 358.7)


        self.frames=[]
        self.frames.append(setup.GRAPHICS['pipe.png'])

        self.frames.append(setup.GRAPHICS['well.png'])
        self.frames.append(setup.GRAPHICS['small_house.png'])

        if self.type==0:
            self.image = self.frames[self.type]
        elif self.type==1:
            self.image=self.frames[self.type]
        elif self.type==2:
            self.image=self.frames[self.type]

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.gravity = C.GRAVITY

        self.state = 'rest'  # 默认状态
        self.timer = 0

    def update(self):
        self.current_time = pygame.time.get_ticks()
        self.handle_states()

    def handle_states(self):
        if self.state == 'rest':
            self.rest()
    def rest(self):
        pass