﻿# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Задача C4-28. 
Решение на языке Python 3.
 Автор: Константин Поляков, 2013
E-mail: kpolyakov@mail.ru
   Web: kpolyakov.spb.ru
-------------------------------------------------
На вход программе подается набор символов, заканчивающийся точкой.
Напишите эффективную, в том числе и по используемой памяти, программу 
(укажите используемую версию языка программирования, например, Borland
Pascal 7.0), которая сначала будет определять, есть ли в этом наборе
символы, соответствующие десятичным цифрам. Если такие символы есть,
то можно ли переставить их так, чтобы полученное число было 
симметричным (читалось одинаково как слева направо, так и справа 
налево). Ведущих нулей в числе быть не должно, исключение – число 0, 
запись которого содержит ровно один ноль. Если требуемое число
составить невозможно, то программа должна вывести на экран слово “NO”.
А если возможно, то в первой строке следует вывести слово “YES”, а во
второй – искомое симметричное число. Если таких чисел несколько, то
программа должна выводить максимальное из них. Например, пусть на вход 
подаются следующие символы: 
    Do not 911 to 09 do.
В данном случае программа должна вывести
    YES
    91019
"""
import sys
save_stdin = sys.stdin
sys.stdin = open("in/28.in")

import string
s = input().split('.')[0]

cnt = {}
for c in s:
    if c in string.digits:
        cnt[c] = cnt.get(c,0) + 1

total = sum([x[1] for x in cnt.items()])            

lWing = ""
for c in string.digits[::-1]:    
    if cnt.get(c) != None:
        while cnt[c] > 1:
            lWing += c
            cnt[c] -= 2

rWing = lWing[::-1]        
for c in string.digits:
    if cnt.get(c) == 1:
        lWing += c
        break
s = lWing + rWing

if total > 0 and s[0] == '0':
    print('Да\n0')   
else:
    if len(s) == total:
        print('Да\n' + s)
    else:
        print('Нет')

sys.stdin = save_stdin