# Задача 9. Вариант 10.
# Создайте игру, в которой компьютер выбирает какое-либо слово, а игрок должен его отгадать. 
# Компьютер сообщает игроку, сколько букв в слове, и дает пять попыток узнать, есть ли какая-либо буква в слове,
# причем программа может отвечать только "Да" и "Нет". Вслед за тем игрок должен попробовать отгадать слово.

# Lisyanskaya A.V.
# 06.04.2017

import random
WORDS = ("месяц", "машина", "весло", "краски", "солнце", "собака", "лес", "шашлык", "природа", "квартира")
word = random.choice(WORDS)
correct = word
print(
"""
                     Добро пожаловать в игру 'Слова'
                 Загадывает слово, а Вы должны его отгадать.
				         Вы будете знать длину слова.
       У вас есть 5 попыток проверить, есть ли какая-либо буква в слове.
          (Если Вы хотите сдаться, не начиная игру, нажмите Enter, не вводя своей версии.)
                                
								Удачи!!!
"""
)
print("\nСлово загадано. В этом слове", len(word), "букв.")
popitka = ()
i = 1
while i <= 5:
    popitka = input("Попробуйте угадать букву из слова: ")
    if popitka in word:
        print("Да")
    if popitka not in word:
        print("Нет")
    i = i + 1
otvet = input("\nПопробуйте отгадать исходное слово: ")
while otvet != correct and otvet != "":
    print("К сожалению, Вы не правы.")
    otvet = input("Попробуйте еще раз: ")
if otvet == correct:
    print("Вы отгадали слово!!!! Поздравляем!!!!")
print("\nСпасибо за игру!")
input("\n\nНажмите Enter, чтобы выйти.")
	
	