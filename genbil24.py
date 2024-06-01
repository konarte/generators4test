#!/usr/bin/env python
import io
import random



import inspect
import os
import sys

def get_script_dir(follow_symlinks=True):
    if getattr(sys, 'frozen', False): # py2exe, PyInstaller, cx_Freeze
        path = os.path.abspath(sys.executable)
    else:
        path = inspect.getabsfile(get_script_dir)
    if follow_symlinks:
        path = os.path.realpath(path)
    return os.path.dirname(path)

#print(get_script_dir())
#print(get_script_dir() + '\\' +'question.txt')



bilet_num = int(input('Какой номер билета будет первым: ').strip() or "1")
#vopr01 - 100 вопросов по 1 баллу в билете - мы их просто удаляем из списка
vopr01=[]
#vopr02 - 11 тем по 1 баллу в билете - мы их тасуеми запоминаем сколько раз какой вопрос всплыл
vopr02=[]

#bilet_num=1


   
def loadfile(path, spisok):
    with io.open(path, encoding='utf-8') as file:
        for line in file:
            spisok.append(line.rstrip())

    
def gen_shu(questions):
    q4 = 'Команды Linux в области: ' + random.choice(questions)
    q5 = 'Команды Linux в области: ' + random.choice(questions)
    if str(q4) == str(q5):
        q4, q5 = gen_shu(questions)
    return (q4, q5)
    
            

print(get_script_dir()+ '\\' +'question.txt')
loadfile(get_script_dir()+ '\\' +'questions.txt', vopr01)
loadfile(get_script_dir()+ '\\' +'questions2.txt', vopr02)


while len(vopr01)>=3:

    random_index = random.randrange(len(vopr01))
    question01 = vopr01.pop(random_index)

    random_index = random.randrange(len(vopr01))
    question02 = vopr01.pop(random_index)
    
    random_index = random.randrange(len(vopr01))
    question03 = vopr01.pop(random_index)

    question04, question05 = gen_shu(vopr02)
    if str(question04) == str(question05):
        print(question04 +' <==> '+ question05)


    print('РОССИЙСКИЙ УНИВЕРСИТЕТ КООПЕРАЦИИ')
    print('Кафедра информационных технологий и ЕНД')
    print('Дисциплина “Инструментальные средства информационных систем”')
    print('Курс 2. Факультет высшего образования')
    print('Специальность “Информационные системы и технологии”')
    print(' ')
    print('Экзаменационный билет № ', bilet_num)
    print(' ')
    print('ВОПРОС 1: ', question01)
    #print(' ')
    print('ВОПРОС 2: ', question02)
    #print(' ')
    print('ВОПРОС 3: ', question03)
    #print(' ')
    print('ВОПРОС 4: ', question04)
    #print(' ')
    print('ВОПРОС 5: ', question05)
    #print(' ')
    print('Утверждено на заседании кафедры протоколом')
    print('     № 1 от 31 августа 2023 г.')
    print('Зав. кафедрой                                        Битюцкий С.Я.')
    print('___________________________________________________________')

    bilet_num += 1

