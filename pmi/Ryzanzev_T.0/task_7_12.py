#Задача 7. Вариант 12

#Создайте игру, в которой компьютер загадывает название одного из двенадцати
#городов, входящих в Золотое кольцо России, а игрок должен его угадать.
#Разработайте систему начисления очков для задачи 6, в соответствии с которой
#игрок получал бы большее количество баллов за меньшее количество попыток.

#Ryazantsev T.O.
#04.03.2017
import random
sobor_list=["Успенский собор",
"Благовещенский собор",
"Архангельский собор"
"Колокольня Ивана Великого",
"Храм Положения ризы Божией Матери во Влахерне",
"Патриарший дворец и собор Двенадцати Апостолов",
"Верхоспасский собор",
"Церковь Рождества Богородицы на Сенях"]
	  
score=0
j=0
while j<3:
    sobor=input("Выберете собор: ")
    i=random.randint(0,7)
    if sobor_list[i]==sobor:
        prize=3/(j+1)
        score=score+prize
        print("Вы выйрали, ваш приз: ",prize,"Ваши очки: ",score)
        j=0
    else:
        print("Вы пройрали, я выбрал",sobor_list[i])
        j+=1
input("Press Enter")