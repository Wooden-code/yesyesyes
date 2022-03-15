
import pygame
from .. import setup,tools
from ..components import enemy
from .. import constants as C

def create_powerup(centerx,centery,type):#根据主角不同状态出不同的东西
    return Mushroom(centerx,centery)




class Powerup(pygame.sprite.Sprite):
    def __init__(self,centerx,centery,frame_rects):
        pygame.sprite.Sprite.__init__(self)

        self.frames=[]
        self.frame_index=0
        for frame_rect in frame_rects:
            self.frames.append(tools.get_image(setup.GRAPHICS['item_objects.png'],*frame_rect,(0,0,0),2.5))
        self.image=self.frames[self.frame_index]
        self.rect=self.image.get_rect()
        self.rect.centerx=centerx
        self.rect.centery=centery
        self.origin_y=centery-self.rect.height/2

        self.x_vel=0
        self.direction=1#向右
        self.y_vel=-1#向上长出来
        self.gravity=1
        self.max_y_vel=8

    def update_position(self, level):
        self.rect.x += self.x_vel
        self.check_x_collisions(level)
        self.rect.y += self.y_vel
        self.check_y_collision(level)

        if self.rect.x<0 or self.rect.y>C.SCREEN_H:
            self.kill()


    def check_x_collisions(self, level):
        sprite = pygame.sprite.spritecollideany(self, level.ground_items_group)
        if sprite:
            self.direction = 1 if self.direction == 0 else 0
            if self.direction:  # 向右#这里主要是龟壳碰撞希望回来
                self.direction = 0
                self.rect.right = sprite.rect.left
            else:
                self.direction = 1
                self.rect.left = sprite.rect.right
            self.x_vel *= -1



    def check_y_collision(self, level):
        check_group = pygame.sprite.Group(level.ground_items_group, level.box_group, level.brick_group)
        sprite = pygame.sprite.spritecollideany(self, check_group)
        if sprite:
            if self.rect.top < sprite.rect.top:
                self.rect.bottom = sprite.rect.top
                self.y_vel = 0
                self.state = 'walk'
        level.check_will_fall(self)

class Mushroom(Powerup):
    def __init__(self,centerx,centery):
        Powerup.__init__(self,centerx,centery,[(0,0,16,16)])
        self.x_vel=2
        self.state='grow'
        self.name='mushroom'

    def update(self,level):

        if self.state=='grow':
            self.rect.y+=self.y_vel
            if self.rect.bottom<self.origin_y:
                self.state='walk'
        elif self.state=='walk':
            pass
        elif self.state=='fall':
            if self.y_vel<self.max_y_vel:
                self.y_vel+=self.gravity
        if self.state!='grow':
           self.update_position(level)

class Fireball(Powerup):
    def __init__(self,centerx,centery,direction):
        frame_rects=[(96,144,8,8),(184,144,8,8),(96,152,8,8),(184,152,8,8),#旋转
                     (112,144,16,16),(112,168,16,16),(112,176,16,16)]#爆炸
        Powerup.__init__(self,centerx,centery,frame_rects)
        self.name='fireball'
        self.state='fly'
        self.direction=direction
        self.x_vel=10 if self.direction else -10
        self.y_vel=0

        self.timer=0

    def update(self,level):
        self.current_time=pygame.time.get_ticks()
        if self.state=='fly':
            self.y_vel=0
            if self.current_time-self.timer>200:
                self.frame_index +=1
                self.frame_index %=4
                self.timer=self.current_time
                self.image=self.frames[self.frame_index]#让火球旋转起来
            self.update_position(level)
        elif self.state=='boom':
            if self.current_time-self.timer>50:
                if self.frame_index<6:
                    self.frame_index+=1
                    self.timer=self.current_time
                    self.image=self.frames[self.frame_index]
                else:
                    self.kill()



    def update_position(self, level):
        self.rect.x += self.x_vel
        self.check_x_collisions(level)
        self.rect.y += self.y_vel
        self.check_y_collision(level)

        if self.rect.x<0 or self.rect.y>C.SCREEN_H:
            self.kill()


    def check_x_collisions(self, level):
        check_group=pygame.sprite.Group(level.ground_items_group,level.enemy_group)
        sprite = pygame.sprite.spritecollideany(self, check_group)
        if sprite:
          self.frame_index=4
          self.state='boom'



    def check_y_collision(self, level):
        check_group = pygame.sprite.Group(level.ground_items_group, level.box_group, level.brick_group)
        sprite = pygame.sprite.spritecollideany(self, check_group)
        if sprite:
            if self.rect.top < sprite.rect.top:
                self.rect.bottom = sprite.rect.top
                self.y_vel = -10#反弹效果





class LifeMushroon(Powerup):
    pass

class Star(Powerup):
    pass

