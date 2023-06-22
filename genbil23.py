#!/usr/bin/env python
import io
import random

#vopr01 - 144 вопроса по 2 в билете - мы их просто удаляем из списка
vopr01=[]
#vopr02 - 26 вопроса по 1 в билете - мы их тасуеми запоминаем сколько раз какой вопрос всплыл
vopr02=[]
#vopr02 - 8 вопросов по 1 в билете - мы их тасуеми запоминаем сколько раз какой вопрос всплыл
vopr03=[]
bilet_num=1


   
def loadfile(path, spisok):
    with io.open(path, encoding='utf-8') as file:
        for line in file:
            spisok.append(line.rstrip())
    
            


loadfile('v01.txt', vopr01)
loadfile('v02.txt', vopr02)
loadfile('v03.txt', vopr03)

while len(vopr01)>0:

    random_index = random.randrange(len(vopr01))
    question01 = vopr01.pop(random_index)

    random_index = random.randrange(len(vopr01))
    question02 = vopr01.pop(random_index)

    random.shuffle(vopr02)
    question03 = random.choice(vopr02)

    random.shuffle(vopr03)
    question04 = random.choice(vopr03)






    print('РОССИЙСКИЙ УНИВЕРСИТЕТ КООПЕРАЦИИ')
    print('Кафедра информационных технологий и ЕНД')
    print('Дисциплина “Инструментальные средства информационных систем”')
    print('Курс 2. Факультет высшего образования')
    print('Специальность “Информационные системы и технологии”')
    print(' ')
    print('Экзаменационный билет № ', bilet_num)
    print(' ')
    print('ВОПРОС 1: ', question01)
    print(' ')
    print('ВОПРОС 2: ',question02)
    print(' ')
    print('ВОПРОС 3: ',question03)
    print(' ')
    print('ЗАДАНИЕ 4: ',question04)
    print(' ')
    print('Утверждено на заседании кафедры протоколом')
    print('     № 1 от 31 августа 2021 г.')
    print('Зав. кафедрой                                        Битюцкий С.Я.')
    print('___________________________________________________________')
    bilet_num += 1





