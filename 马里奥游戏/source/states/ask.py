import pygame,os
from .. import setup  # ..是上一级文件
from .. import tools
from .. import constants as C
from ..components import info  # 到上一级目录平行的components
import random

def gogo(num):
    if num==1:
        fii='eat.ogg'
    elif num==2:
        fii='drop.ogg'
    abs = os.getcwd()
    sds = abs.split(r'\\')
    ewr = sds[0] + r'\\resource\\music\\'+fii
    try:
        pygame.mixer.Sound(ewr).play()
    except:
        ewr = sds[0].split('dist')[0] + r'resource\\music\\' + fii
        pygame.mixer.Sound(ewr).play()
    return 0


class Ask:
    i = 0
    instance = None
    expanded_i = 1
    before_i=-1
    ct=0

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


        self.explanation1=[setup.GRAPHICS['question1_1.png']]
        self.explanation2 =[setup.GRAPHICS['question2_1.png'],setup.GRAPHICS['question2_2.png'],setup.GRAPHICS['question2_3.png'],setup.GRAPHICS['question2_4.png']]
        self.explanation3 = [setup.GRAPHICS['question3_1.png'],setup.GRAPHICS['question3_2.png']]

        self.frames_answer=[setup.GRAPHICS['answer1.png'],setup.GRAPHICS['answer2.png'],setup.GRAPHICS['answer3.png']]
        self.frames_explanation=[self.explanation1,self.explanation2,self.explanation3]



        # self.ask6 = setup.GRAPHICS['ask_6.png']
        self.frames = [self.ask0, self.ask1, self.ask2]
        self.answer_rects = [(489, 470, 509, 488), (489, 499,509, 516),(489, 529, 509, 546), (489, 560, 509, 575)]
        self.answer_dict = {'0': 0,
                            '1': 2,
                            '2': 1}

        self.setup_background()

        self.finished = False  # 只要这个阶段还在运行就不完结
        self.next = 'load_screen'

    def setup_background(self):  # 设置底图\\

        self.num =random.randint(0,2)
        self.background = self.frames[self.num]  #
        self.background_rect = self.background.get_rect()
        self.background = pygame.transform.scale(self.background, (
            int(self.background_rect.width * C.BG_W_MULTI), int(self.background_rect.height * C.BG_H_MULTI)))
        self.viewport = setup.SCREEN.get_rect()  # 滑动窗口
        self.game_ground = pygame.Surface((self.background_rect.width, self.background_rect.height))

    curTime = None

    def update(self, surface,flag):  # 更新操作

        surface.blit(self.background, (450, 179.5))
        # check_0= tools.button(*self.answer_rects[0])#检查各个选项
        # check_1= tools.button(*self.answer_rects[1])
        # check_2= tools.button(*self.answer_rects[2])
        # check_3= tools.button(*self.answer_rects[3])
        self.answer = self.answer_dict[str(self.num)]  # 记录正确答案对应的选项
        check_right = tools.button(*self.answer_rects[self.answer])
        self.time = pygame.time.get_ticks()
        #print(pygame.mouse.get_pos())
        #if self.curTime!=None:
            #if pygame.time.get_ticks() - self.curTime > 5000:
                #for explanation in self.frames_explanation[self.num]:
                #    if self.frames_explanation[self.num].index(explanation)==0:
                #        surface.blit(explanation, (450, 179.5))

                        #os.system('pause')
                 #   elif pygame.mouse.get_pressed():
                  #      surface.blit(explanation, (450, 179.5)) #做一个点击任意继续
                        #os.system('pause')



        #print(check_right)
        if check_right == 8 and self.ct==0:
            #print((self.answer_rects[self.num])[0],(self.answer_rects[self.num])[0])
            #pygame.transform.scale(self.frames_answer[self.num], (1, 1))
            self.background.blit(self.frames_answer[self.num],(-4,17))
            self.ct+=1

            #if self.curTime == None:
           #     self.curTime = pygame.time.get_ticks()

        elif check_right == 6:
            self.finished = True
            self.next = 'main_menu'

        #if pygame.mouse.get_pressed() == (1, 0, 0):
        #    surface.blit(self.frames_explanation[self.num][i], (450, 179.5))
        #   i += 1
        mouse = pygame.mouse.get_pressed()
        #print(mouse)
        #self.before_i = self.i-1
        if mouse == (1, 0, 0) and self.i < len(self.frames_explanation[self.num]) and check_right!=8 and self.ct!=0 and self.before_i<self.i:
            gogo(2)
            self.before_i=self.i
            pygame.time.wait(500)
            self.background.blit(self.frames_explanation[self.num][self.i], (0, 0))
            self.i += 1

            # print(i)
        elif mouse == (1, 0, 0) and self.i == len(self.frames_explanation[self.num]):
            gogo(2)
            self.i=0
            self.ct=0
            self.before_i=-1
            self.finished = True
            self.next = 'level'
            self.game_info['num'] = 0
            # self.finished = True

            # self.next = 'level'
            self.curTime = None

    def draw(self, surface):
        self.game_ground.blit(self.background, (472.5, 290))


