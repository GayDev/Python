# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Задача C4-30. 
Решение на языке Python 3.
 Автор: Константин Поляков, 2013
E-mail: kpolyakov@mail.ru
   Web: kpolyakov.spb.ru
-------------------------------------------------
На вход программе подаются сведения о ячейках камеры хранения багажа.
В первой строке – текущая дата – день (ровно две цифры, от 01 до 31),
затем через точку – месяц (ровно две цифры, от 01 до 12). Во второй 
строке сообщается количество занятых ячеек N (не меньше 3, но не
больше 1000). Каждая из следующих строк имеет формат: 
    <номер ячейки> <дата сдачи багажа>
Номер ячейки – это целое число, дата – 5 символов: день (ровно две
цифры, от 01 до 31), затем через точку – месяц (ровно две цифры, от 01
до 12). Сведения отсортированы по номерам ячеек. Все даты относятся к 
одному календарному году. Считать, что в феврале 28 дней. 
Нужно вывести номера тех ячеек, в которых багаж хранится более 3 дней
в хронологическом порядке сдачи багажа. Например, если исходные данные
были такие:
    04.06 
    3
    1000 01.06
    1001 31.05
    2007 21.05
то результат должен быть следующий:
    2007
    1001
"""
import sys
save_stdin = sys.stdin
sys.stdin = open("in/30.in")

def date2dist ( date ):
    daysIn = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    d, m = int(date[0:2]), int(date[3:])
    dist = d
    for i in range(m):
        dist += daysIn[i]
    return dist

curDate = date2dist(input())
N = int(input())

cells = {}
for i in range(N):
    cellNo, cellDate = input().split()
    cells[cellNo] = cellDate

moreThan3days = [x for x in cells.items() if curDate-date2dist(x[1]) > 3]
moreThan3days.sort(key = lambda x: date2dist(x[1]))
for x in moreThan3days:
    print(x[0])

sys.stdin = save_stdin