import pygame, os, sys
class Block():
    def __init__(self, cords, width, height, color,copyColor):
        self.x=cords[0]
        self.y=cords[1]
        self.h=height
        self.w=width
        self.image=pygame.Surface((width, height), pygame.SRCALPHA)
        self.color=color
        self.second_color = (255,0,0)
        self.draw()
        self.originalColor=copyColor
    def changeColor(self, cords, ):

        if self.collidePoint(cords) == True:
            # color=self.color
            # newColor=(100,0,0)
            # self.color=newColor
            self.color, self.second_color=self.second_color, self.color
            self.draw()

    def moveON(self,moveTo):#Передвижение блока
        self.x += moveTo[0]
        self.y += moveTo[1]
        return self.x, self.y

    def collidePoint (self, cords): #Сопаставляет координаты мыши с координатами объекта
        if (cords[0] > self.x and cords[0] < self.x + self.w) and (cords[1] > self.y and cords[1] < self.y + self.h):
            return True
        else:
            return False

    def get_cords(self):#Возвращает координаты текущего объекта.
        return self.x, self.y

    def draw(self):#Рисует фигуры на указанных поверхностях.
        pygame.draw.rect(self.image,self.color, (0, 0, self.h, self.w))

    def events(self, e):#Обрабатывает события  влияющие на объект.
        if e.type == pygame.MOUSEBUTTONDOWN:
            self.changeColor(e.pos)
        if e.type == pygame.MOUSEMOTION:
            self.moveON(e.rel)

        pass

    def update(self):
        pass

    def render(self, screen):#Отображает объект на экране.
        screen.blit(self.image,(self.x,self.y))

#Main

"""
Создание окна
"""
pygame.init() #инициализация
display = pygame.display.set_mode((400, 400)) #создание окна

"""
Содание объектов
"""
first=Block((100, 10), 80, 100, (0,0,0), (0,0,0))
second=Block((100, 100), 90, 40, (0,101,20), (0,101,20))
third=Block((23, 150), 45, 40, (101,101,101),(101,101,101))

while True:  #главный цикл программы
    for e in pygame.event.get(): #цикл обработки очереди событий окна
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                sys.exit()
        if e.type == pygame.QUIT:
            sys.exit()
        if e.type == pygame.MOUSEBUTTONDOWN:
            print(e)
            print(first.events(e))
            print(second.events(e))
            print(third.events(e))

         #if e.type == pygame.MOUSEMOTION:
            #first.events(e)
            #second.events(e)
            #third.events(e)
            # print(e)
            # print(first.moveON(e.rel,))
            pass

    display.fill((0,0,100))
    first.render(display)
    second.render(display)
    third.render(display)
    pygame.display.flip()










