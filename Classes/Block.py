import pygame
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
        self.small_rect=self.image.get_rect()
        self.small_rect.left=self.rect.w-10
        self.small_rect.top=self.rect.h-10
        self.small_rect.h=10
        self.small_rect.w=10
        self.color=color
        self.second_color = (255,0,0)
        self.draw()
        self.originalColor=color
        self.drag=False
        self.deformation=False


    def conver_to_local(self, coord):
        """ Преобразует преданные координаты в локальные"""


        return coord[0]- self.rect.x, coord[1]-self.rect.y

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
        self.small_rect = pygame.Rect(self.rect.w-10, self.rect.h-10, 10,10)
        pygame.draw.rect(self.image,(12,233,34), self.small_rect)

    def events(self, e):#Обрабатывает события  влияющие на объект.
        if e.type == pygame.MOUSEBUTTONDOWN:
            self.changeColor(e.pos)
            if self.small_rect.collidepoint(self.conver_to_local(e.pos)):
                print("Click on small")
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
                # self.small_rect=self.small_rect.move(e.rel)
                # self.draw()
                self.image=self.image=pygame.Surface((self.rect.w, self.rect.h), pygame.SRCALPHA)
                self.draw()
        if e.type == pygame.MOUSEBUTTONUP:
            self.drag = False
            self.deformation=False

    def update(self):
        pass

    def render(self, screen):#Отображает объект на экране.
        screen.blit(self.image,(self.rect.left,self.rect.top))

