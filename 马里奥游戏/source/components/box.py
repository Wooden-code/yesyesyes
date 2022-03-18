from .. import tools, setup
import pygame
from .. import constants as C
from .powerup import create_powerup

class Box(pygame.sprite.Sprite):
    def __init__(self,x,y,box_type,group,name='box'):
        #pygame.sprite.Sprite.__init__(self)
        #self.x=x
        #self.y=y
        #self.box_type=box_type
        #self.group=group
        #self.name=name
        #self.frame_rects={
            #(384,0,16,16),
            #(400,0,16,16),
            #(416,0,16,16),
            #(432,0,16,16)
        #}

        #self.frames=[]
        #for frame_rect in self.frame_rects:
        #    self.frames.append(tools.get_image(setup.GRAPHICS['tile_set.png'],*frame_rect,(0,0,0),C.BRICK_MULTI))

        #self.frame_index=1
        #self.image=self.frames[self.frame_index]
        #self.rect=self.image.get_rect()
        #self.rect.x=self.x
        #self.rect.y=self.y
        #self.gravity=C.GRAVITY

        #self.state='rest'#默认状态
        #self.timer=0
        pass

    def update(self):
        #self.current_time=pygame.time.get_ticks()
        #self.handle_states()
        pass
    def handle_states(self):
        #if self.state=='rest':
        #    self.rest()
        #elif self.state=='bumped':
        #    self.bumped()
        #elif self.state=='open':
        #   self.open()
        pass

    def rest(self):
        #frame_durations=[400,100,100,50]#休息状态也要自动闪烁
        #if self.current_time-self.timer>frame_durations[self.frame_index]:
        #    self.frame_index=(self.frame_index+1)%4
        #    self.timer=self.current_time
        #self.image=self.frames[self.frame_index]
        pass

    def go_bumped(self):
        #self.y_vel=-7
        #self.state='bumped'
        pass
    def bumped(self):
        #self.rect.y+=self.y_vel
        #self.y_vel+=self.gravity
        #self.frame_index=3
        #self.image=self.frames[self.frame_index]

        #if self.rect.y>self.y+10:#这里加一个10相当于多掉下10再回来，显得动画更流畅
        #    self.rect.y=self.y#不让宝箱掉下来
        #    self.state='open'
        pass
            #被顶起后判断宝箱的类型 0 无，1 金币，2 星星，3 蘑菇
            #if self.box_type==1:
            #    pass
            #else:
            #    self.group.add(create_powerup(self.rect.centerx,self.rect.centery,self.box_type))

    def open(self):
        pass
