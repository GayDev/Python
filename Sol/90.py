# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Задача C4-90. 
Решение на языке Python 3.
Автор: Александр Жуков, 2018
-------------------------------------------------
90) (А. Жуков) На вход программы подается натуральное число N, 
а затем N целых чисел. Необходимо определить максимальное произведение 
смежных элементов последовательности. N не превышает 1000, каждый 
элемент последовательности не превосходит по модулю 100.
Пример входных данных:
7
2
3
-2
-3
-1
4
6
Пример выходных данных:
72
Пояснения: наибольшее произведение можно получить для 
последовательности -3 -1 4 6.
"""
import sys
save_stdin = sys.stdin
sys.stdin = open("in/90.in")

n = int(input())
dp_min = dp_max = mx = x = int(input())
for i in range(n-1):
  x = int(input())
  t = min(dp_min*x, min(dp_max*x, x))
  dp_max = max(dp_min*x, max(dp_max*x, x))
  dp_min = t
  mx = max(mx, dp_max)
print(mx)

sys.stdin = save_stdin