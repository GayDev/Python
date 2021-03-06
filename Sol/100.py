# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Задача C4-100.
Решение на языке Python 3.
-------------------------------------------------
100) (А.А. Богданов – Danov1900 №27-2) На вход 
программы поступает последовательность из N целых 
положительных чисел. Рассматриваются все пары 
различных элементов последовательности (элементы 
пары не обязаны стоять в последовательности рядом, 
порядок элементов в паре неважен). Необходимо 
определить количество произвольных пар, произведение 
чисел и разность индексов которых кратна 3.
Описание входных и выходных данных
В первой строке входных данных задаётся количество 
чисел N (1 ≤ N ≤ 10000). В каждой из последующих N 
строк записано одно натуральное число, не превышающее 
10000. В качестве результата программа должна вывести 
одно число: количество найденных пар.
Пример входных данных №1:
10 
1 2 3 4 5 6 7 8 9 10
Выходные данных для приведенного выше примера: 
3
найденные пары: (3;6), (3;9), (6;9)
Пример входных данных №2: 
30 
4 8 6 7 4 6 8 6 9 8 3 2 7 1 8 4 4 1 6 7 1 3 8 5 6 2 5 5 9 6
Выходные данных для приведенного выше примера:
78
"""
import sys
save_stdin = sys.stdin
sys.stdin = open("in/100.in")

def sign( n ):
  if n > 0: return 1
  elif n < 0: return -1
  else: return 0

k = [ [0,0,0], [0,0,0], [0,0,0] ]

n = int( input() )

for i in range(n):
  a = int( input() )
  k[sign(a % 3)][i % 3] += 1

s = 0
for j in range(3):
  s += k[0][j]*(k[0][j]-1) // 2 + k[0][j]*k[1][j]

print( s )

sys.stdin = save_stdin