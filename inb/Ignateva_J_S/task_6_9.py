#Задание 6. Вариант 9.
#Создайте игру, в которой компьютер загадывает имя одного из трех поросят,
#а игрок должен его угадать.

#Ignateva J.S
#28.03.2017
import random
print('Программа загадывает одного из трех поросят, пользователю предоставляется возможность отгадать загаданного персонажа')
porks= ('Ниф-ниф','Наф-наф','Нуф-нуф')
computer =porks[random.randint(0,2)]
user = ''
while user != computer:
    user = (input('Угадайте какого поросенка загадал компьютер: '))
    if user == computer:
        print ('Верно!Это',computer)
        break
    else:
         print ('К сожалению вы не угадали, попробуйте еще раз')
input ('Нажмите Enter для выхода')
