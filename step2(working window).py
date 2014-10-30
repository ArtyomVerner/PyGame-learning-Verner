# -*- coding: utf-8 -*-
import pygame

pygame.init() #инициализация
display = pygame.display.set_mode((400,400)) #создание окна

done = False
while not done: #главный цикл программы
    for e in pygame.event.get(): #цикл обработки очереди событий окна
        print(e.type)
        if e.type == 12: #Обработка события "Закрытие окна"
            print(pygame.QUIT)
            done = True
        elif e.type==pygame.MOUSEBUTTONDOWN:
            print("Нажата клавиша мыши")
