# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Задача C4-84. 
Решение на языке Python 3.
 Автор: Константин Поляков, 2018
-------------------------------------------------
84) На вход программы поступает последовательность 
из N целых положительных чисел. Из них нужно выбрать и вывести 
два числа так, чтобы их сумма была нечётна, а произведение делилось 
на 5 и при этом было максимально возможным. Выбранные числа можно 
выводить в любом порядке. Если есть несколько подходящих пар, можно 
выбрать любую из них. Если подходящих пар нет, нужно вывести 0.
Описание входных и выходных данных 
В первой строке входных данных задаётся количество чисел N (1 ≤ N ≤ 1000). 
В каждой из последующих N строк записано одно натуральное число, не 
превышающее 100. 
Пример входных данных:
5
1
2
3
4
5
Пример выходных данных для приведённого выше примера входных данных:
4 5
Из 5 чисел можно составить 10 пар. В данном случае условиям удовлетворяют 
две пары: (2, 5) и (4, 5). Суммы чисел в этих парах (7 и 9) нечётны, а 
произведения (10 и 20) делятся на 5. У всех остальных пар как минимум 
одно из этих условий не выполняется. Из этих пар выбрана пара с наибольшим 
произведением.
"""
import sys
save_stdin = sys.stdin
sys.stdin = open("in/84.in")

max_xx = max_2x = max_x5 = max_10 = 0
N = int(input())
for i in range(0, N) :
  x = int(input())
  if x % 2 == 0 and x % 5 == 0:
    max_10 = max(max_10, x)
  elif x % 2 == 0:
    max_2x = max(max_2x, x)
  elif x % 5 == 0:
    max_x5 = max(max_x5, x)
  else:
    max_xx = max(max_xx, x)

max_xx = max(max_xx, max_x5)
if max_xx*max_10 > max_2x*max_x5:
  r1, r2 = max_xx, max_10
else:
  r1, r2 = max_2x, max_x5
if r1 == 0:
  print(0)
else:
  print(r1, r2)

sys.stdin = save_stdin