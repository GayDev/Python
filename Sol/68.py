# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Задача C4-68. 
Решение на языке Python 3.
 Автор: Константин Поляков, 2017
E-mail: kpolyakov@mail.ru
   Web: kpolyakov.spb.ru
-------------------------------------------------
68) На вход программы поступает последовательность из 
N натуральных чисел. Требуется определить, с какой 
цифры реже всего (но, по крайней мере, один раз) 
начинается десятичная запись этих чисел. Если таких 
цифр несколько, необходимо вывести наименьшую из них.
Входные данные:
  На вход программе подаётся натуральное число N 
  (N <= 1000), а затем N натуральных чисел, каждое из 
  которых не превышает 10000. 
Пример входных данных: 
3 
13
214
32
Выходные данные:
  Программа должна вывести одну (минимальную) цифру, 
  с которой реже всего начинаются введённые числа. 
Пример выходных данных для приведённого примера входных данных: 
1
"""
import sys
save_stdin = sys.stdin
sys.stdin = open("in/68.in")

count = [0]*10
def Digits(x):
  global count
  while x > 10:
    x //= 10
  count[x] += 1

N = int(input())
for i in range(N):
  x = int(input())
  Digits(x)
  
M = min( [x for x in range(10) if count[x] > 0] )
print( count.index(M) )

sys.stdin = save_stdin