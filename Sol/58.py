# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Задача C4-58. 
Решение на языке Python 3.
 Автор: Константин Поляков, 2015
E-mail: kpolyakov@mail.ru
   Web: kpolyakov.spb.ru
-------------------------------------------------
Для заданной последовательности неотрицательных целых 
чисел необходимо найти максимальное произведение двух её 
элементов, номера которых различаются не менее чем на 8. 
Значение каждого элемента последовательности не 
превышает 1000. Количество элементов последовательности 
не превышает 10000.
Входные данные представлены следующим образом. В первой 
строке задаётся число N – общее количество элементов 
последовательности. Гарантируется, что N > 8. В каждой 
из следующих N строк задаётся одно неотрицательное 
целое число – очередной элемент последовательности. 
Пример входных данных:
10
100
45
55
245
35
25
10
10
10
26
Программа должна вывести одно число – 
описанное в условии произведение.
Пример выходных данных для приведённого выше 
примера входных данных:
2600
"""
import sys
save_stdin = sys.stdin
sys.stdin = open("in/58.in")

N = int(input())
K = 8
Buf = [0]*K
maxPrev = 0
maxRes = 0
for i in range(N):
  if i >= K:
    maxPrev = max(maxPrev, Buf[i % K])
  Buf[i % K] = int(input())
  maxRes = max(maxRes, maxPrev*Buf[i % K])

print(maxRes)

sys.stdin = save_stdin