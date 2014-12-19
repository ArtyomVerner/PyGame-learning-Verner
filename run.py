import pygame, sys
from Classes.Block import Block

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










