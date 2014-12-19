import pygame, sys
from Utilities.loads import load_image
def hello_world():
    print("Hello World")

class Text:   #простой класс, для вывода текста
    def __init__(self, text, color = (0,0,0), font = None, font_size = 24):
        self.text = text
        self.font = pygame.font.Font(font, font_size)
        self.color = color

    def render(self):
        """
        Возвращает картинку с текстом
        """
        return self.font.render(self.text, True, self.color)



class Button ():
    def __init__(self, coord, text, font_size):
        b_off=load_image('button_off.png', path='../Images/Buttons', alpha_cannel=True)
        b_click=load_image('button_click.png', path='../Images/Buttons', alpha_cannel=True)
        b_hover=load_image('button_hover.png', path='../Images/Buttons', alpha_cannel=True)
        self.img_num=0
        self.images=[b_off, b_click, b_hover]
        self.rect=self.images[self.img_num].get_rect()
        self.rect.x=coord[0]
        self.rect.y=coord[1]
        self.text = Text(text=text, font_size=font_size).render()
        self.text_size=self.text.get_size()


    def events(self, e):
        if e.type == pygame.MOUSEBUTTONUP:
            self.img_num=0
            # if self.rect.collidepoint(e.pos):
            #     self.but_hover=True

        if e.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(e.pos):
                self.img_num=1
                a=hello_world
                a()
        if e.type == pygame.MOUSEMOTION:
            if self.rect.collidepoint(e.pos):
                self.img_num=2
            else:
                self.img_num = 0


    def update(self):
        pass
    def render(self,screen):
        screen.blit(self.images[self.img_num],(self.rect.left,self.rect.top))
        screen.blit(self.text, (self.rect.left+(self.rect.w/2)-(self.text_size[0]/2),
                                self.rect.top+(self.rect.h/2)-(self.text_size[1]/2)))
"""Main"""
pygame.init() #инициализация
display = pygame.display.set_mode((400, 400)) #создание окна
button1=Button((200, 200), "Button", 40)
while True:  #главный цикл программы
    for e in pygame.event.get(): #цикл обработки очереди событий окна
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                sys.exit()
        if e.type == pygame.QUIT:
            sys.exit()

        if e.type == pygame.MOUSEBUTTONDOWN:
            button1.events(e)

        if e.type == pygame.MOUSEBUTTONUP:
            button1.events(e)
        if e.type == pygame.MOUSEMOTION:
            button1.events(e)
        """
        Отображение объектов
        """

    display.fill((0,0,100))
    button1.render(display)
    pygame.display.flip()







