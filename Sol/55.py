# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Задача C4-55. 
Решение на языке Python 3.
 Автор: Константин Поляков, 2014
E-mail: kpolyakov@mail.ru
   Web: kpolyakov.spb.ru
-------------------------------------------------
На вход программы подаются результаты измерений, выполняемых 
прибором с интервалом 1 минуту. Все данные – натуральные 
числа, не превышающие 1000. Требуется найти наименьшую сумму 
квадратов двух результатов измерений, выполненных с интервалом 
не менее, чем в 5 минут. 
Описание входных данных
В первой строке вводится одно натуральное число – количество 
измерений N. Гарантируется, что 5 < N <= 10000. Каждая из 
следующих N строк содержит по одному натуральному числу – 
результат очередного измерения.
Описание выходных данных
Программа должна вывести одно число наименьшую сумму 
квадратов двух результатов измерений, выполненных с интервалом 
не менее, чем в 5 минут.
Пример входных данных:
  9
  12
  45
  5
  4
  21
  20
  10
  12
  26
Пример выходных данных для приведённого выше примера входных данных:
  169
"""
import sys
save_stdin = sys.stdin
sys.stdin = open("in/55.in")

N = int(input())
K = 5
Buf = [0]*K
minPrev = 1001
minRes = 2*1000**2 + 1
for i in range(N):
  if i >= K:
    minPrev = min(minPrev, Buf[i % K])
  Buf[i % K] = int(input())
  minRes = min(minRes, minPrev**2 + Buf[i % K]**2)

print(minRes)

sys.stdin = save_stdin