# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Задача C4-32. 
Решение на языке Python 3.
 Автор: Константин Поляков, 2013
E-mail: kpolyakov@mail.ru
   Web: kpolyakov.spb.ru
-------------------------------------------------
Некоторый поезд в пути следования останавливается на N станциях (станция
номер 1 — начальная, а станция номер N — конечная). Дан список
пассажиров поезда, для каждого из которых известно, на какой станции он 
садится, а на какой — выходит. Напишите эффективную по времени работы и 
используемой памяти программу, которая по этим данным определяет, на 
каких перегонах (то есть между какими соседними станциями) в поезде было 
наименьшее число пассажиров. На вход программе в первой сроке подается
количество станций N и количество пассажиров P. В каждой из последующих
P строк находится информация о пассажирах в следующем формате:
    <Фамилия> <Имя> <станция посадки> <станция выхода>
где <Фамилия> – строка, состоящая не более, чем из 20 символов без 
пробелов, <Имя> – строка, состоящая не более, чем из 20 символов без
пробелов, <станция посадки> и <станция выхода> — числа от 1 до N, при 
этом номер станции посадки меньше номера станции выхода.
Пример входных данных:
    6 3
    Иванов Сергей 2 4
    Сергеев Петр 1 3
    Петров Кирилл 3 6
Программа должна вывести список перегонов, на которых в поезде было
наименьшее число пассажиров. Каждый перегон выводится в виде двух 
последовательных номеров станций, разделенных знаком “-“. Для примера
выше результат работы программы должен быть таким (на данных перегонах в 
поезде находилось наименьшее число пассажиров):
    1-2
    4-5
    5-6
При выполнении задания следует учитывать, что значение N не превосходит
10, а значение P может быть большим (до 1000).
"""
import sys, codecs
save_stdin = sys.stdin
sys.stdin = codecs.open("in/32.in", "r", "utf-8")

N, P = input().split()
N, P = int(N), int(P)
cnt = [0] * (N-1)
for i in range(P):
    fam, name, pFrom, pTo = input().split()
    pFrom, pTo = int(pFrom), int(pTo)
    for p in range(pFrom, pTo):
        cnt[p-1] += 1

pMin = min(cnt)
for p in range(N-1):
    if cnt[p] == pMin:
        print("%d-%d" % (p+1, p+2))

sys.stdin = save_stdin