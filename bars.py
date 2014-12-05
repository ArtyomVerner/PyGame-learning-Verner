import pygame, os, sys
class Block():#Класс Блок
    def __init__(self, coords, width, height, color,):
        """
        Метод конструктор
        """
        # self.x=cords[0]
        # self.y=cords[1]
        # self.h=height
        # self.w=width
        self.image=pygame.Surface((width, height), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.left=coords[0]
        self.rect.top=coords[1]
        self.rect.h=height
        self.rect.w=width
        self.color=color
        self.second_color = (255,0,0)
        self.draw()
        self.originalColor=color
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
        if (cords[0] > (self.rect.w-10)+self.rect.left and cords[0] < self.rect.w+self.rect.left) \
                and (cords[1] > (self.rect.h-10)+self.rect.top and cords[1] < self.rect.h+self.rect.top):
            return True
        else:
            return False


    def changeColor(self, cords):
        """
        Метод изменяет цвет объекта
        """
        if self.rect.collidepoint(cords):
            self.color, self.second_color = self.second_color, self.color
            self.draw()


    # def get_cords(self):#Возвращает координаты текущего объекта.
    #     return self.x, self.y

    def draw(self):#Рисует фигуры на указанных поверхностях.
        pygame.draw.rect(self.image,self.color, (0, 0, self.rect.w,  self.rect.h))
        pygame.draw.rect(self.image,(12,233,34), (self.rect.w-10, self.rect.h-10, 10, 10))

    def events(self, e):#Обрабатывает события  влияющие на объект.
        if e.type == pygame.MOUSEBUTTONDOWN:
            self.changeColor(e.pos)
            if self.collidePoint2(e.pos):
                self.deformation=True


            # self.drag_and_drop(e)
            elif self.rect.collidepoint(e.pos):
                self.drag = True
                return self



        if e.type == pygame.MOUSEMOTION:
            # self.moveON(e.rel)
            # print(self.d)
            if self.drag:
                self.rect = self.rect.move(e.rel)
            elif self.deformation:
                self.rect.w+=e.rel[0]
                self.rect.h+=e.rel[1]
                if self.rect.w < 10:
                    self.rect.w=10
                if self.rect.h < 10:
                    self.rect.h=10
                self.image=self.image=pygame.Surface((self.rect.w, self.rect.h), pygame.SRCALPHA)
                self.draw()
        if e.type == pygame.MOUSEBUTTONUP:
            self.drag = False
            self.deformation=False

    def update(self):
        pass

    def render(self, screen):#Отображает объект на экране.
        screen.blit(self.image,(self.rect.left,self.rect.top))

#Main

"""
Создание окна
"""
pygame.init() #инициализация
display = pygame.display.set_mode((400, 400)) #создание окна

"""
Содание объектов
"""
first=Block((100, 10), 80, 100, (0,0,0))
second=Block((100, 100), 90, 40, (0,101,20))
third=Block((23, 150), 45, 40, (101,101,101))
fourth=Block((40, 66,), 8, 12, (12, 103, 234))
fifth=Block((34, 76,), 28, 12, (1, 103, 234))
sixth=Block((44, 86,), 38, 12, (12, 103, 234))
seventh=Block((90, 96,), 48, 12, (12, 103, 234))
eighth=Block((104, 106,), 28, 12, (12, 103, 234))
ninth=Block((29, 116,), 58, 12, (12, 103, 234))
tenth=Block((88, 236,), 68, 12, (12, 103, 234))
objects = [first, second, third, fourth, fifth, sixth, seventh, eighth, ninth, tenth]
while True:  #главный цикл программы
    for e in pygame.event.get(): #цикл обработки очереди событий окна
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                sys.exit()
        if e.type == pygame.QUIT:
            sys.exit()

        if e.type == pygame.MOUSEBUTTONDOWN:
            for el in objects:
                if el.events(e):
                    print("click on", el)
                    helper=el
                    objects.remove(el)
                    objects.append(el)
                    break


        if e.type == pygame.MOUSEBUTTONUP:
            for el in objects:
                el.events(e)


        if e.type == pygame.MOUSEMOTION:
            for el in objects:
                el.events(e)

            pass
        """
        Отображение объектов
        """

    display.fill((0,0,100))
    for el in objects:
        el.render(display)
    pygame.display.flip()










