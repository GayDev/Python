# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Задача C4-103.
Решение на языке Python 3.
-------------------------------------------------
103) (О.Л. Дуркин) 
На вход программы поступает последовательность 
из N натуральных чисел (6 ≤ N ≤ 10000). Необходимо 
определить минимальную разность двух элементов этой 
последовательности, такую,  что эта разность кратна 3 
и расстояние между двумя элементами не менее 5. 
Если таких пар нет, программа должна вывести слово NO.
Описание входных и выходных данных
В первой строке входных данных задается количество чисел N. 
В каждой из последующих N строк записано одно натуральное 
число, не превосходящее 1000. Программа должна вывести 
одно число – минимальную разность удовлетворяющую условию 
или «NO», если такую разность получить нельзя.
Пример входных данных:
  10
  1 
  2 
  3 
  4 
  5 
  6 
  7 
  8 
  9 
  10
Пример выходных данных для приведенного выше примера входных данных:
  -9
"""
import sys
save_stdin = sys.stdin
sys.stdin = open("in/103.in")

mi = 3*[1001]
ma = 3*[0]
min_sub = 1001

n = int(input())

a = 6*[0]
for i in range(5):
 a[i] = int(input())
 
for i in range(5, n):
  a[5] = int(input())
  if a[0] > ma[a[0]%3]: 
    ma[a[0]%3] = a[0]
  if a[0] < mi[a[0]%3]: 
    mi[a[0]%3] = a[0]
  if (a[5]-ma[a[5]%3]) < min_sub and \
     ma[a[5]%3] != 0: 
    min_sub = a[5] - ma[a[5]%3]
  if (mi[a[5]%3]-a[5]) < min_sub and mi[a[5]%3] != 1001:    
    min_sub = mi[a[5]%3] - a[5]
  for j in range(5):
    a[j] = a[j+1]

if min_sub == 1001:
  print( "NO" )
else:
  print( min_sub )

sys.stdin = save_stdin