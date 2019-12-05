# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Задача C4-98.
Решение на языке Python 3.
-------------------------------------------------
98) (А.А. Богданов – Danov1802 №27-5) На вход 
программы поступает последовательность из N целых 
положительных чисел. Рассматриваются все пары 
различных элементов последовательности (элементы 
пары не обязаны стоять в последовательности рядом, 
порядок элементов в паре неважен). Необходимо 
определить минимальную сумму произвольной пары чисел 
и количество пар с суммой равной минимальной. 
Описание входных и выходных данных
В первой строке входных данных задаётся количество 
чисел N (1 ≤ N ≤ 10000). В каждой из последующих N 
строк записано одно натуральное число, не превышающее 
10000. В качестве результата программа должна вывести 
два числа: найденную минимальную сумму и количество 
пар с суммой равной минимальной.
Пример входных данных №1: 
10 
1 2 3 1 2 3 1 2 3 1
Выходные данных для приведенного выше примера: 2 6
Пример входных данных №2: 
5 
2 2 1 2 2
Выходные данных для приведенного выше примера: 3 4
"""
import sys
save_stdin = sys.stdin
sys.stdin = open("in/98.in")

n = int( input() )
m1 = m2 = 10001
k1 = 0

for i in range(n):
  a = int( input() )
  if a < m1:
    m2 = m1
    k2 = k1
    m1 = a
    k1 = 0
  elif a < m2:
    m2 = a
    k2 = 0  
  if a == m1:
    k1 += 1 
  if a == m2: 
    k2 += 1

if m1 == m2:
  k = k1*(k1-1) // 2
else: 
  k = k2
  
print( m1+m2, k ) 

sys.stdin = save_stdin