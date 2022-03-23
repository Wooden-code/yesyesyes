import pygame,os
from .. import setup  # ..是上一级文件
from .. import tools
from .. import constants as C
from ..components import info  # 到上一级目录平行的components
import random


class Ask:
    instance = None
    expanded_i = 1

    def __init__(self):
        game_info = {
            'score': 0,
            'coin': 0,
            'lives': 3,
            'player_state': 'small'  # 大的还是小的什么的

        }
        self.start(game_info)

    def start(self, game_info):
        self.game_info = game_info

        self.ask0 = setup.GRAPHICS['question1.png']
        self.ask1 = setup.GRAPHICS['question2.png']
        self.ask2 = setup.GRAPHICS['question3.png']


        #self.explanation1=setup.GRAPHICS[]
        #self.explanation2 = setup.GRAPHICS[]
        #self.explanation3 = setup.GRAPHICS[]

        self.frames_answer=[pygame.image.load(os.path.abspath("resource/graphics/answer1.png")),pygame.image.load(os.path.abspath("resource/graphics/answer2.png")),pygame.image.load(os.path.abspath("resource/graphics/answer3.png"))]
        #self.frames_explanation=[self.explanation1,self.explanation2,self.explanation3]



        # self.ask6 = setup.GRAPHICS['ask_6.png']
        self.frames = [self.ask0, self.ask1, self.ask2]
        self.answer_rects = [(468, 436, 503, 453), (468, 473,503, 490),(468, 509, 503, 530), (468, 545, 503, 560)]
        self.answer_dict = {'0': 0,
                            '1': 2,
                            '2': 1}

        self.setup_background()

        self.finished = False  # 只要这个阶段还在运行就不完结
        self.next = 'load_screen'

    def setup_background(self):  # 设置底图\\
        self.num = random.randint(0, 2)
        self.background = self.frames[self.num]  #
        self.background_rect = self.background.get_rect()
        self.background = pygame.transform.scale(self.background, (
            int(self.background_rect.width * C.BG_W_MULTI), int(self.background_rect.height * C.BG_H_MULTI)))
        self.viewport = setup.SCREEN.get_rect()  # 滑动窗口
        self.game_ground = pygame.Surface((self.background_rect.width, self.background_rect.height))

    curTime = None

    def update(self, surface, keys):  # 更新操作

        surface.blit(self.background, (450, 179.5))
        # check_0= tools.button(*self.answer_rects[0])#检查各个选项
        # check_1= tools.button(*self.answer_rects[1])

        # check_2= tools.button(*self.answer_rects[2])
        # check_3= tools.button(*self.answer_rects[3])
        self.answer = self.answer_dict[str(self.num)]  # 记录正确答案对应的选项
        check_right = tools.button(*self.answer_rects[self.answer])
        self.time = pygame.time.get_ticks()
        print(pygame.mouse.get_pos())
        if self.curTime!=None:
            if pygame.time.get_ticks() - self.curTime > 5000:
                #surface.blit(self.explanation[self.num], (450, 179.5)) #做一个点击任意继续
                #mouse=pygame.mouse.get_pressed()
                #if mouse:

                self.finished = True
                self.game_info['num']=0
                self.next = 'level'
                self.curTime = None
        print(check_right)
        if check_right == 8:
            print((self.answer_rects[self.num])[0],(self.answer_rects[self.num])[0])
            #pygame.transform.scale(self.frames_answer[self.num], (1, 1))
            self.background.blit(self.frames_answer[self.num],(-2,-65))

            if self.curTime == None:
                self.curTime = pygame.time.get_ticks()

        elif check_right == 6:
            self.finished = True
            self.next = 'main_menu'

    def draw(self, surface):
        self.game_ground.blit(self.background, (472.5, 290))

class End:
    instance = None
    expanded_i = 1

    def __init__(self):
        game_info = {
            'score': 0,
            'coin': 0,
            'lives': 3,
            'player_state': 'small'  # 大的还是小的什么的

        }
        self.start(game_info)

    def start(self, game_info):
        self.game_info = game_info

        self.ask0 = setup.GRAPHICS['question1.png']
        self.ask1 = setup.GRAPHICS['question2.png']
        self.ask2 = setup.GRAPHICS['question3.png']

        self.answer1=setup.GRAPHICS['answer1.png']
        self.answer2=setup.GRAPHICS['answer2.png']
        self.answer3 = setup.GRAPHICS['answer3.png']

        self.frames_answer=[self.answer1,self.answer2,self.answer3]



        # self.ask6 = setup.GRAPHICS['ask_6.png']
        self.frames = [self.ask0, self.ask1, self.ask2]
        self.answer_rects = [(468, 436, 503, 453), (468, 473,503, 490),(468, 509, 503, 530), (468, 545, 503, 560)]
        self.answer_dict = {'0': 0,
                            '1': 2,
                            '2': 1}

        self.setup_background()

        self.finished = False  # 只要这个阶段还在运行就不完结
        self.next = 'load_screen'

    def setup_background(self):  # 设置底图\\
        self.num = random.randint(0, 2)
        self.background = self.frames[self.num]  #
        self.background_rect = self.background.get_rect()
        self.background = pygame.transform.scale(self.background, (
            int(self.background_rect.width * C.BG_W_MULTI), int(self.background_rect.height * C.BG_H_MULTI)))
        self.viewport = setup.SCREEN.get_rect()  # 滑动窗口
        self.game_ground = pygame.Surface((self.background_rect.width, self.background_rect.height))

    curTime = None

    def update(self, surface, keys):  # 更新操作

        surface.blit(self.background, (450, 179.5))
        # check_0= tools.button(*self.answer_rects[0])#检查各个选项
        # check_1= tools.button(*self.answer_rects[1])

        # check_2= tools.button(*self.answer_rects[2])
        # check_3= tools.button(*self.answer_rects[3])
        self.answer = self.answer_dict[str(self.num)]  # 记录正确答案对应的选项
        check_right = tools.button(*self.answer_rects[self.answer])
        self.time = pygame.time.get_ticks()
        print(pygame.mouse.get_pos())
        if self.curTime!=None:
            if pygame.time.get_ticks() - self.curTime > 8000:

                self.finished = True
                self.next = 'level'
                self.curTime = None
        print(check_right)
        if check_right == 8:
            print((self.answer_rects[self.num])[0],(self.answer_rects[self.num])[0])
            #pygame.transform.scale(self.frames_answer[self.num], (1, 1))
            self.background.blit(self.frames_answer[self.num],(-2,-65))

            if self.curTime == None:
                self.curTime = pygame.time.get_ticks()

        elif check_right == 6:
            self.finished = True
            self.next = 'main_menu'

    def draw(self, surface):
        self.game_ground.blit(self.background, (472.5, 290))


