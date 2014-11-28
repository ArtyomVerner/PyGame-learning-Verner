import pygame, os, sys
class Block():#Класс Блок
    def __init__(self, cords, width, height, color,copyColor):
        """
        Метод конструктор
        """
        self.x=cords[0]
        self.y=cords[1]
        self.h=height
        self.w=width
        self.image=pygame.Surface((self.w, self.h), pygame.SRCALPHA)
        self.color=color
        self.second_color = (255,0,0)
        self.draw()
        self.originalColor=copyColor
        self.drag=False
        self.deformation=False

    # def drag_and_drop(self, e):
    #     """
    #     Принимает:
    #     Событие нажатия мыши
    #     Событие передвижения мыши
    #
    #     При захвате объекта мышкой, метод перемещает объект в соответствие с перемещением мыши
    #     """
    #     if self.collidePoint(e.pos):
    #         self.drag = True
    #
    #         #print("First", self.drag)
    #         if pygame.MOUSEBUTTONUP:
    #             self.drag = False
    #             #print("Second", self.drag)


    def collidePoint2 (self, cords):
        if (cords[0] > (self.w-10)+self.x and cords[0] < self.w+self.x) \
                and (cords[1] > (self.h-10)+self.y and cords[1] < self.h+self.y):
            return True
        else:
            return False


    def changeColor(self, cords):
        """
        Метод изменяет цвет объекта
        """
        if self.collidePoint(cords):
            self.color, self.second_color = self.second_color, self.color
            self.draw()

    def moveON(self,dCoords):#Передвижение блока
        self.x += dCoords[0]
        self.y += dCoords[1]

    def collidePoint (self, cords): #Сопаставляет координаты мыши с координатами объекта
        if (cords[0] > self.x and cords[0] < self.x + self.w) and (cords[1] > self.y and cords[1] < self.y + self.h):
            return True
        else:
            return False

    def get_cords(self):#Возвращает координаты текущего объекта.
        return self.x, self.y

    def draw(self):#Рисует фигуры на указанных поверхностях.
        pygame.draw.rect(self.image,self.color, (0, 0, self.w,  self.h))
        pygame.draw.rect(self.image,(12,233,34), (self.w-10, self.h-10, 10, 10))

    def events(self, e):#Обрабатывает события  влияющие на объект.
        if e.type == pygame.MOUSEBUTTONDOWN:
            self.changeColor(e.pos)
            if self.collidePoint2(e.pos):
                self.deformation=True


            # self.drag_and_drop(e)
            elif self.collidePoint(e.pos):
                self.drag = True



        if e.type == pygame.MOUSEMOTION:
            # self.moveON(e.rel)
            # print(self.d)
            if self.drag:
                self.moveON(e.rel)
            elif self.deformation:
                self.resize(e.rel)

        if e.type == pygame.MOUSEBUTTONUP:
            self.drag = False
            self.deformation=False

    def update(self):
        pass

    def render(self, screen):#Отображает объект на экране.
        screen.blit(self.image,(self.x,self.y))


    def resize(self, rel):

        """
        Изменяет размер блока
        """
        self.w+=rel[0]
        self.h+=rel[1]
        self.image=pygame.Surface((self.w, self.h), pygame.SRCALPHA)
        self.draw()
        if self.w <= 10:
            self.w=10
        if self.h <= 10:
            self.h=10



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
            # print(e)
            first.events(e)
            second.events(e)
            third.events(e)


        if e.type == pygame.MOUSEBUTTONUP:
            first.events(e)
            second.events(e)
            third.events(e)

        if e.type == pygame.MOUSEMOTION:

            first.events(e)
            second.events(e)
            third.events(e)
            # print(e)
            # print(first.moveON(e.rel,))
            pass
        """
        Отображение объектов
        """

    display.fill((0,0,100))
    first.render(display)
    second.render(display)
    third.render(display)
    pygame.display.flip()










