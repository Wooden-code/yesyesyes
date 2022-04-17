
import pygame
from .. import tools,setup
from .. import constants as C
import json
import os
from ..components import powerup

class Player(pygame.sprite.Sprite):
    num=0
    def __init__(self,name):
        self.name='boyu'
        self.load_data()
        self.setup_states()
        self.setup_velocities()
        self.setup_timers()
        self.load_images()

    def load_data(self):#json文件被转化为了python中的字典 载入玩家的json文件  共同的json
        file_name=self.name+'.json'
        # file_path=os.path.join('source/data/player',file_name)#拼出文件路径
        #TODO:path
        file_path=r'C:\Users\abc\Desktop\yesyesyes\马里奥游戏\source\data\player\boyu.json'
        with open(file_path,encoding='utf-8-sig',errors='ignore') as f:
            self.player_data=json.load(f,strict=False)#加载后的文件就是一个字典


    def setup_states(self):#主角状态
        self.face_right=True#脸朝右
        self.dead=False#死亡
        self.big=False#变大状态
        self.state='stand'#最开始是站立的状态
        self.can_jump=True
        self.can_shoot=True
        self.hurt_immune=False#刚出生的时候肯定不能免疫伤害



    def setup_velocities(self):#设置速度
        speed=self.player_data['speed']
        self.x_vel=0
        self.y_vel=0

        self.max_walk_vel=speed['max_walk_speed']#速度
        self.max_run_vel=speed['max_run_speed']
        self.max_y_vel=speed['max_y_velocity']
        self.jump_vel=speed['jump_velocity']
        self.walk_accel=speed['walk_accel']#加速度
        self.turn_accel=speed['turn_accel']#急刹车转身时的速度
        self.run_accel=speed['run_accel']
        self.gravity=C.GRAVITY
        self.anti_gravity=C.ANTI_GRAVITY

        self.max_x_vel=self.max_walk_vel#初始的最大速度为步行速度
        self.x_accel=self.walk_accel#初始加速度为步行加速度



    def setup_timers(self):#创建一系列的计时器
        self.walking_timer=0#走路时长
        self.transition_timer=0#变身时长
        self.dead_timer=0
        self.hurt_immune_timer=0
        self.last_fireball_timer=0


    def load_images(self):#主角的各种帧造型
        boyu_day_normal_1=setup.GRAPHICS['boyu_day_normal_1.png']
        boyu_day_normal_2 = setup.GRAPHICS['boyu_day_normal_2.png']
        boyu_day_normal_3 = setup.GRAPHICS['boyu_day_normal_3.png']
        boyu_day_normal_4 = setup.GRAPHICS['boyu_day_normal_4.png']
        boyu_day_normal_5 = setup.GRAPHICS['boyu_day_normal_5.png']
        boyu_day_normal_6 = setup.GRAPHICS['boyu_day_normal_6.png']
        boyu_day_normal_7 = setup.GRAPHICS['boyu_day_normal_7.png']
        boyu_day_normal_8 = setup.GRAPHICS['boyu_day_normal_8.png']
        boyu_day_normal_9 = setup.GRAPHICS['boyu_day_normal_9.png']
        boyu_day_normal_10 = setup.GRAPHICS['boyu_day_normal_10.png']


        boyu_day_special_1 = setup.GRAPHICS['boyu_day_special_1.png']
        boyu_day_special_2 = setup.GRAPHICS['boyu_day_special_2.png']
        boyu_day_special_3 = setup.GRAPHICS['boyu_day_special_3.png']
        boyu_day_special_4 = setup.GRAPHICS['boyu_day_special_4.png']
        boyu_day_special_5 = setup.GRAPHICS['boyu_day_special_5.png']
        boyu_day_special_6 = setup.GRAPHICS['boyu_day_special_6.png']
        boyu_day_special_7 = setup.GRAPHICS['boyu_day_special_7.png']
        boyu_day_special_8 = setup.GRAPHICS['boyu_day_special_8.png']
        boyu_day_special_9 = setup.GRAPHICS['boyu_day_special_10.png']
        boyu_day_special_10 = setup.GRAPHICS['boyu_day_special_10.png']

        boyu_night_normal=setup.GRAPHICS['boyu_night_normal.png']
        boyu_night_special=setup.GRAPHICS['boyu_night_special.png']
        frame_rects = self.player_data['image_frames']

        self.right_day_normal_frames = [boyu_day_normal_1,boyu_day_normal_2,boyu_day_normal_3,boyu_day_normal_4,boyu_day_normal_5,boyu_day_normal_6,boyu_day_normal_7,boyu_day_normal_8,boyu_day_normal_9,boyu_day_normal_10]#区分开来的格格帧库 最底层
        self.right_night_normal_frames = []
        self.right_day_special_frames = [boyu_day_special_1,boyu_day_special_2,boyu_day_special_3,boyu_day_special_4,boyu_day_special_5,boyu_day_special_6,boyu_day_special_7,boyu_day_special_8,boyu_day_special_9,boyu_day_special_10]
        self.right_night_special_frames=[]
        self.left_day_normal_frames = [pygame.transform.flip(boyu_day_normal_1, True, False),pygame.transform.flip(boyu_day_normal_2, True, False),pygame.transform.flip(boyu_day_normal_3, True, False),pygame.transform.flip(boyu_day_normal_4, True, False),pygame.transform.flip(boyu_day_normal_5, True, False),pygame.transform.flip(boyu_day_normal_6, True, False),pygame.transform.flip(boyu_day_normal_7, True, False),pygame.transform.flip(boyu_day_normal_8, True, False),
                                       pygame.transform.flip(boyu_day_normal_9, True, False), pygame.transform.flip(boyu_day_normal_10, True, False)]
        self.left_night_normal_frames = []
        self.left_day_special_frames = [pygame.transform.flip(boyu_day_special_1,True,False),pygame.transform.flip(boyu_day_special_2,True,False),pygame.transform.flip(boyu_day_special_3,True,False),pygame.transform.flip(boyu_day_special_4,True,False),pygame.transform.flip(boyu_day_special_5,True,False),pygame.transform.flip(boyu_day_special_6,True,False),pygame.transform.flip(boyu_day_special_7,True,False),pygame.transform.flip(boyu_day_special_8,True,False),
                                        pygame.transform.flip(boyu_day_special_9,True,False),pygame.transform.flip(boyu_day_special_10,True,False)]
        self.left_night_special_frames=[]

        self.day_normal_frames=[self.right_day_normal_frames,self.left_day_normal_frames]
        self.night_normal_frames=[self.right_night_normal_frames,self.left_night_normal_frames]#中间层
        self.day_special_frames=[self.right_day_special_frames,self.left_day_special_frames]
        self.night_special_frames=[self.right_night_special_frames,self.left_night_special_frames]

        self.all_frames=[#最大一层
            self.right_day_normal_frames ,
        self.right_night_normal_frames ,
        self.right_day_special_frames,
        self.right_night_special_frames,
        self.left_day_normal_frames ,
        self.left_night_normal_frames,
        self.left_day_special_frames,
        self.left_night_special_frames

        ]


        for group,group_frame_rects in frame_rects.items():#遍历键值对 将得到的帧图分门别类放入帧库
            for frame_rect in group_frame_rects:


                if group=='right_day_normal':
                    pass
                if group=='right_night_normal':
                    right_image = tools.get_image(boyu_night_normal, frame_rect['x'], frame_rect['y'],
                                                  frame_rect['width'],
                                                  frame_rect['height'], (0, 0, 0), C.PLAYER_MULTI)
                    left_image = pygame.transform.flip(right_image, True, False)
                    self.right_night_normal_frames.append(right_image)
                    self.left_night_normal_frames.append(left_image)
                if group=='right_day_special':
                    pass
                if group=='right_night_special':
                    right_image = tools.get_image(boyu_night_special, frame_rect['x'], frame_rect['y'],
                                                  frame_rect['width'],
                                                  frame_rect['height'], (0, 0, 0), C.PLAYER_MULTI)
                    left_image = pygame.transform.flip(right_image, True, False)
                    self.right_night_special_frames.append(right_image)
                    self.left_night_special_frames.append(left_image)

        self.right_frames = self.right_day_normal_frames  # 默认的右的帧库
        self.left_frames = self.left_day_normal_frames

        self.frame_index = 0
        self.frames=self.right_frames
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()


    def update(self,keys,surfacewwwwwwwww,level):#keys指的是按键
        self.current_time=pygame.time.get_ticks()#人物帧的更新
        self.handle_states(keys,level)
        self.is_hurt_immune()

    def handle_states(self,keys,level):#处理状态

        self.can_jump_or_not(keys)
        self.can_shoot_or_not(keys)

        if self.state=='stand':
            self.stand(keys,level)
        elif self.state=='walk':#也就是到哪个状态用调哪个函数
            self.walk(keys,level)
        elif self.state=='jump':
            self.jump(keys,level)
        elif self.state=='fall':
            self.fall(keys,level)
        elif self.state=='die':
            self.die(keys)
        elif self.state=='hurt':
            # print('yyyyyyy')
            self.hurt(keys,level)
        elif self.state=='small2big':
            self.small2big(keys)
        elif self.state=='big2small':
            self.big2small(keys)
        elif self.state=='re_blood':
            self.re_blood(keys,level)
        #else:
        #    self.state=None
        if self.face_right:
            self.image=self.right_frames[self.frame_index]
        else:
            self.image=self.left_frames[self.frame_index]

    def can_jump_or_not(self,keys):
        if not keys[pygame.K_UP]:
            self.can_jump=True


    def can_shoot_or_not(self,keys):
        if not keys[pygame.K_SPACE]:
            self.can_shoot=True



    def stand(self,keys,level):
        self.frame_index=0
        self.x_vel=0
        self.y_vel=0
        # self.can_jump=True
        if keys[pygame.K_RIGHT]:
            self.face_right=True
            self.state='walk'
        elif keys[pygame.K_LEFT]:
            self.face_right=False
            self.state='walk'
            #and self.can_jump
        elif keys[pygame.K_UP] :
            self.state='jump'
            self.y_vel=self.jump_vel
        elif keys[pygame.K_SPACE] and self.can_shoot:#设置空格键
            self.shoot_fireball(level)
        elif keys[pygame.K_w] :
            if level.if_change==True:

                self.state='re_blood'
                self.re_timer=pygame.time.get_ticks()

            #level.change=False
        #print(level.if_change)

    def walk(self,keys,level):

        if keys[pygame.K_s]:
            self.max_x_vel=self.max_run_vel
            self.x_accel=self.run_accel
        else:
            self.max_x_vel=self.max_walk_vel
            self.x_accel=self.walk_accel

        if self.current_time-self.walking_timer>600:#self.calc_frame_duration():
            if self.frame_index<2:
                self.frame_index+=1
            else:
                self.frame_index=1
            self.walking_timer=self.current_time

        if keys[pygame.K_UP] and self.can_jump:
            self.state='jump'
            self.y_vel=self.jump_vel

        elif keys[pygame.K_RIGHT]:
            self.face_right = True
            if self.x_vel < 0:
                self.frame_index = 0
                self.x_accel = self.turn_accel
            self.x_vel = self.calc_vel(self.x_vel, self.x_accel, self.max_x_vel, True)
        elif keys[pygame.K_LEFT]:
            self.face_right = False
            if self.x_vel > 0:
                self.frame_index = 0
                self.x_accel = self.turn_accel
            self.x_vel = self.calc_vel(self.x_vel, self.x_accel, self.max_x_vel, False)

        elif keys[pygame.K_SPACE] and self.can_shoot:  # 设置空格键
            self.shoot_fireball(level)
        elif not keys[pygame.K_UP] and not keys[pygame.K_LEFT]:
            if self.face_right:
                self.x_vel -= self.x_accel
                if self.x_vel < 0:
                    self.x_vel = 0
                    self.state = 'stand'
            else:
                self.x_vel += self.x_accel
                if self.x_vel > 0:
                    self.x_vel = 0
                    self.state = 'stand'
        else:#这里判断不是很准确，我们希望不按任何键人物停下来，但这里的判断是不按指定的键其他任何键人物才能停下来 处理方法可以选定一个键专门用来停下（如果无法做到自动停下的话
            if self.face_right:
                self.x_vel -= self.x_accel
                if self.x_vel<0:
                    self.x_vel=0
                    self.state='stand'
            else:
                self.x_vel += self.x_accel
                if self.x_vel > 0:
                    self.x_vel = 0
                    self.state = 'stand'



    def jump(self,keys,level):
        self.frame_index=3
        self.y_vel+=self.anti_gravity
        self.can_jump=False#一旦起跳便不能继续起跳


        if self.y_vel >= 0:
            self.state='fall'

        if keys[pygame.K_RIGHT]:
            self.x_vel=self.calc_vel(self.x_vel,self.x_accel,self.max_x_vel,True)
        elif keys[pygame.K_LEFT]:
            self.x_vel=self.calc_vel(self.x_vel,self.x_accel,self.max_x_vel,False)
        elif keys[pygame.K_SPACE] and self.can_shoot:  # 设置空格键
            self.shoot_fireball(level)

        if not keys[pygame.K_UP]:
            self.state = 'fall'

    def fall(self,keys,level):
        self.x_vel=self.x_vel
        self.y_vel=self.calc_vel(self.y_vel,self.gravity,self.max_y_vel)

        if keys[pygame.K_RIGHT]:
           self.x_vel=self.calc_vel(self.x_vel,self.x_accel,self.max_x_vel,True)
        elif keys[pygame.K_LEFT]:
           self.x_vel=self.calc_vel(self.x_vel,self.x_accel,self.max_x_vel,False)
        if keys[pygame.K_SPACE] and self.can_shoot:  # 设置空格键
            self.shoot_fireball(level)

        if self.x_vel>0:
            self.state='walk'
        else:
            self.state='stand'
        self.state='walk'
        if self.y_vel==0:
            self.can_jump=True

    def re_blood(self,keys,level):
        #print(self.re_timer)
        if pygame.time.get_ticks()-self.re_timer>2000:
            if level.lives<3:
                level.lives=level.lives+1
            level.change.kill()
            self.state='stand'
        else:
            self.frame_index=9





    def die(self,keys):
        self.rect.y+=self.y_vel
        self.y_vel+=self.anti_gravity

    def hurt(self,keys, level):
        self.frame_index=8
        pygame.time.wait(100)
        self.state='hurt'
        # print('aaaaaaaaaaaaa')
        self.x_vel = 0
        self.y_vel = 0
        # self.can_jump=True
        if keys[pygame.K_RIGHT]:
            self.face_right = True
            self.state = 'walk'
        elif keys[pygame.K_LEFT]:
            self.face_right = False
            self.state = 'walk'
            # and self.can_jump
        elif keys[pygame.K_UP]:
            self.state = 'jump'
            self.y_vel = self.jump_vel
        elif keys[pygame.K_SPACE] and self.can_shoot:  # 设置空格键
            self.shoot_fireball(level)

    def go_die(self):
        self.dead=True
        self.y_vel=self.jump_vel
        self.frame_index=4
        self.state='die'
        self.death_timer=self.current_time


    def small2big(self,keys):
        frame_dur=100
        sizes=[1,0,1,0,1,2,0,1,2,0,2]#0 small 1 medium 2 big
        frames_and_idx=[(self.day_normal_frames,0),(self.day_normal_frames,7),(self.day_special_frames,0)]
        if self.transition_timer==0:
            self.big=True
            self.transition_timer=self.current_time
            self.changing_idx=0
        elif self.current_time-self.transition_timer>frame_dur:
            frames, idx = frames_and_idx[sizes[self.changing_idx]]

            self.change_player_image(frames,idx)
            self.changing_idx += 1
            self.transition_timer=self.current_time

            if self.changing_idx ==len(sizes):#如果是变身阶段最后一帧
                self.transition_timer = 0
                self.state = 'walk'
                self.right_frames = self.right_day_special_frames
                self.left_frames = self.left_day_special_frames

    def big2small(self,keys):
        frame_dur=100
        sizes=[2,1,0,1,0,1,0,1,0,1,0]#0 small 1 medium 2 big
        # frames_and_idx=[(self.day_normal_frames,7),(self.day_special_frames,7),(self.day_special_frames,4)]
        frames_and_idx = [(self.day_special_frames, 0), (self.day_special_frames, 7), (self.day_normal_frames, 0)]
        if self.transition_timer==0:
            self.big=False
            self.transition_timer=self.current_time
            self.changing_idx=0
        elif self.current_time-self.transition_timer>frame_dur:
            frames, idx = frames_and_idx[sizes[self.changing_idx]]

            self.change_player_image(frames,idx)
            self.changing_idx += 1
            self.transition_timer=self.current_time

            if self.changing_idx ==len(sizes):#如果是变身阶段最后一帧
                self.transition_timer = 0
                self.state = 'walk'
                self.right_frames = self.right_day_normal_frames
                self.left_frames = self.left_day_normal_frames


    def change_player_image(self,frames,idx):#利用帧造型组和序号给人物换上正确皮肤
        self.frame_index=idx
        if self.face_right:#根据面部朝向取出对应帧
            self.right_frames=frames[0]
            self.image=self.right_frames[self.frame_index]
        else:
            self.left_frames_frames=frames[1]
            self.image=self.left_frames[self.frame_index]
        last_frame_bottom=self.rect.bottom#无论如何变身都默认从脚底出发
        last_frame_centerx=self.rect.centerx
        self.rect=self.image.get_rect()
        self.rect.bottom=last_frame_bottom
        self.rect.centerx=last_frame_centerx




    def calc_vel(self,vel,accel,max_vel,is_positive=True):#分别告诉 速度 加速度 最大速度 速度方向 用来计算速度大小
        if is_positive:#如果方向为正
            return min(vel+accel,max_vel)#每次都加上一个加速度 且不能超过最大速度
        else:
            return max(vel-accel,-max_vel)

    def calc_frame_duration(self):
        duration = -60/self.max_run_vel*abs(self.x_vel)+80#计算帧切换间隔，速度越快间隔越短
        return duration



    def is_hurt_immune(self):#时刻判断无敌状态有没有结束
        if self.hurt_immune:
            if self.hurt_immune_timer==0:
                self.hurt_immune_timer=self.current_time#开始jishi
                self.blank_image=pygame.Surface((1,1))#空白帧
            elif self.current_time- self.hurt_immune_timer<2000:#无敌状态解除后维持的无敌时间
                if (self.current_time-self.hurt_immune_timer)%100<50:#取余 有几个阶段空白帧
                    self.image=self.blank_image#人物空白吧
            else:
                self.hurt_immune=False
                self.hurt_immune_timer=0

    def shoot_fireball(self,level):
         if self.big==False:
            self.frame_index=5#注意这里是发大招的姿势
         elif self.big==True:
             self.frame_index=7
         if self.current_time-self.last_fireball_timer>300:
            fireball=powerup.Fireball(self.rect.centerx,self.rect.centery,self.face_right)#火球是pygame中的精灵
            level.powerup_group.add(fireball)#把发射火球这个方法传入level中的这个组中
            self.can_shoot=False
            self.last_fireball_timer=self.current_time





