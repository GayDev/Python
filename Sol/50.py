﻿# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Задача C4-50. 
Решение на языке Python 3.
 Автор: Константин Поляков, 2013
E-mail: kpolyakov@mail.ru
   Web: kpolyakov.spb.ru
-------------------------------------------------
Радиотелескоп пытается получать и анализировать сигналы из космоса.
Различные шумы переводятся в последовательность вещественные
неотрицательные числа, заданные с точностью до 1 знака после десятичной
точки. Для того чтобы описывать различные участки космоса, данные, 
получаемые из одного района, было решено характеризовать числом, равным
максимальному произведению, которое можно получить, перемножая значения
сигналов, приходящих из этого района. То есть требуется выбрать такое 
непустое подмножество сигналов (в него может войти как один сигнал, так и
все поступившие сигналы), произведение значений у которого будет
максимальным. Если таких подмножеств несколько, то выбрать можно любое из
них. 
Напишите эффективную, в том числе по используемой памяти, программу
(укажите используемую версию языка программирования, например, Borland
Pascal 7.0), которая будет обрабатывать результаты эксперимента, находя 
искомое подмножество. Сигналов может быть очень много, но не может быть
меньше трех. Все сигналы различны. 
Перед текстом программы кратко опишите используемый вами алгоритм решения 
задачи. 
На вход программе в первой строке подается количество сигналов N. В каждой 
из последующих N строк записано одно вещественное число с точностью до 1 
знака после десятичной точки. Все числа различны. 
Пример входных данных: 
5 
12.3 
0.1 
100.2 
0.3 
1.4 
Программа должна вывести в порядке возрастания номера сигналов,
произведение которых будет характеризовать данную серию. Нумерация сигналов
ведется с единицы. 
Пример выходных данных для приведенного выше примера входных данных: 
1 3 5 
"""
import sys
save_stdin = sys.stdin
sys.stdin = open("in/50.in")

N = int(input())
Max = 0; iMax = -1
small = []
for i in range(N):
    x = float(input())
    if x > Max:
        Max = x
        iMax = i
    if x < 1: small.append(i)
if len(small) == N:
    print(iMax+1)
elif len(small) == 0:    
    for i in range(N): print(i+1, end=" ")
else:
    for i in range(N): 
        if not i in small:
            print(i+1, end=" ")

sys.stdin = save_stdin