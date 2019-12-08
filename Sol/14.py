﻿# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Задача C4-14. 
Решение на языке Python 3.
 Автор: Константин Поляков, 2013
E-mail: kpolyakov@mail.ru
   Web: kpolyakov.spb.ru
-------------------------------------------------
На вход программы подаются прописные латинские буквы, ввод этих
символов заканчивается точкой. Напишите эффективную по времени работы 
и по используемой памяти программу (укажите используемую версию языка 
программирования, например, Borland Pascal 7.0), которая будет
определять, можно ли переставить эти буквы так, чтобы получился
палиндром (палиндром читается одинаково слева направо и справа
налево). Программа должна вывести ответ «Да» или «Нет», а в случае
ответа «Да» – еще и сам полученный палиндром (первый в алфавитном
порядке). 
Пример входной строки: 
    GAANN. 
Пример выходных данных: 
    Да
    ANGNA
"""
import sys
save_stdin = sys.stdin
sys.stdin = open("in/14.in")

s = sorted(input().split('.')[0], reverse = True)

middle = ""
res = ""
while len(s) > 0:
    n = s.count(s[0])
    if n % 2 == 0:
        wing = s[0]*(n // 2)
        res = wing + res
    else:
        if middle != "": break
        middle = s[0]*n
    s[0:n] = []
    
if len(s) > 0:
    print("Нет")
else:
    res = res + middle + res[::-1]
    print("Да")
    print(res)

sys.stdin = save_stdin