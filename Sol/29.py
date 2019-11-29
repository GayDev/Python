﻿# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Задача C4-29. 
Решение на языке Python 3.
 Автор: Константин Поляков, 2013
E-mail: kpolyakov@mail.ru
   Web: kpolyakov.spb.ru
-------------------------------------------------
На вход программе подается последовательность символов, среди которых
могут быть и цифры, заканчивающаяся точкой. Требуется написать
программу, которая составляет и выводит минимальное число из тех цифр,
которые не встречаются во входных данных. Ноль не используется. Если
во входных данных встречаются все цифры от 1 до 9, то следует вывести
«0». Например, если исходная последовательность была такая:
    1A734B39. 
то результат должен быть следующий:
    2568
"""
import sys
save_stdin = sys.stdin
sys.stdin = open("in/29.in")

s = input().split('.')[0]

import string
cnt = {}
for d in "123456789": cnt[d] = 0
for c in s:
    if c in string.digits:
        cnt[c] += 1

notFound = [x[0] for x in cnt.items() if x[1] == 0]
if len(notFound) == 0:
    print(0)
else:
    for x in sorted(notFound):
        print(x, end = "")

sys.stdin = save_stdin