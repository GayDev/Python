# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Задача C4-20. 
Решение на языке Python 3.
 Автор: Константин Поляков, 2013
E-mail: kpolyakov@mail.ru
   Web: kpolyakov.spb.ru
-------------------------------------------------
Имеется список учеников разных школ, сдававших экзамен по информатике,
с указанием их фамилии, имени, школы и набранного балла. Напишите
эффективную по времени работы и по используемой памяти программу
(укажите используемую версию языка программирования, например,
Borland Pascal 7.0), которая будет определять двух учеников школы 
№ 50, которые лучше всех сдали информатику, и выводить на экран их
фамилии и имена. 
Если наибольший балл набрали более двух человек, нужно вывести только
их количество. Если наибольший балл набрал один человек, а следующий 
балл набрало несколько человек, нужно вывести только фамилию и имя
лучшего. Известно, что информатику сдавали не менее 5 учеников школы
№ 50.
На вход программе в первой строке подается количество учеников списке
N. В каждой из последующих N строк находится информация в следующем 
формате:
    <Фамилия> <Имя> <Школа> <Балл>
где <Фамилия> – строка, состоящая не более, чем из 20 символов без
пробелов, <Имя> – строка, состоящая не более, чем из 20 символов без
пробелов, <Школа> – целое число от 1 до 99, <Балл> – целое число от 1
до 100.
Пример входной строки:
    Иванов Сергей 50 87
Пример выходных данных, когда найдено два лучших:
    Иванов Сергей
    Сергеев Иван
Если больше двух учеников набрали высший балл, то программа должна
вывести их количество. Пример вывода в этом случае:
    8
Если высший балл набрал один человек, а следующий балл набрало
несколько человек, то программа должна вывести только фамилию и имя
лучшего. Пример вывода в этом случае:
    Иванов Сергей
"""
import sys, codecs
save_stdin = sys.stdin
sys.stdin = codecs.open("in/20.in", "r", "utf-8")

N = int(input())
res = []
for i in range(N):
    fam, name, sch, ball = input().split()
    if sch == "50":
        res.append( (int(ball), fam+" "+name) )
res.sort(reverse = True)
nBest = [x[0] for x in res].count(res[0][0])
if nBest > 2:
    print(nBest)
elif nBest == 1 and len(res) > 2 and res[1][0] == res[2][0]:
    print(res[0][1])
else:
    print( "%s\n%s" % (res[0][1], res[1][1]) )

sys.stdin = save_stdin