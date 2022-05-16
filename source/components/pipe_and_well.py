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



        self.frames=[]

        self.frames.append(setup.GRAPHICS['change_gate.png'])




        self.image=self.frames[0]

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
