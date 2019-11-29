# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Задача C4-88. 
Решение на языке Python 3.
Автор: Александр Жуков, 2018
-------------------------------------------------
88) 88)	(А. Жуков) Вам посчастливилось узнать стоимость акций 
некоторой компании в каждый из ближайших N дней. Какой наибольший 
доход Вы сможете получить, если за все дни возможны не более одной 
покупки и не более одной продажи акций. N не превышает 1000. 
Стоимость акции – натуральное число условных единиц (у.е.), 
меньшее, чем 10000.
Пример входных данных:
9
10
2
5
4
8
7
1
6
4
Пример выходных данных:
6
Пояснения: выгоднее всего купить акцию по 2 у.е. и затем продать по 8 у.е.
"""
import sys
save_stdin = sys.stdin
sys.stdin = open("in/88.in")

n = int(input())
prev = int(input())
mx = dp = 0
for i in range(n-1):
  cur = int(input())
  dp = max(dp, 0) + cur - prev
  mx = max(mx, dp)
  prev = cur
print(mx)

sys.stdin = save_stdin