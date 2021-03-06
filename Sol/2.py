﻿# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Задача C4-2. 
Решение на языке Python 3.
 Автор: Константин Поляков, 2013
E-mail: kpolyakov@mail.ru
   Web: kpolyakov.spb.ru
-------------------------------------------------
На вход программы подается текст на английском языке, заканчивающийся
точкой (другие символы “.” в тексте отсутствуют). Требуется написать
программу, которая будет определять и выводить на экран английскую
букву, встречающуюся в этом тексте чаще всего, и количество там таких
букв. Строчные и прописные буквы при этом считаются не различимыми.
Если искомых букв несколько, то программа должна выводить на экран
первую из них по алфавиту. Например, пусть файл содержит следующую
запись: 
     It is not a simple task. Yes! 
Чаще всего здесь встречаются буквы I, S и T (слово Yes в подсчете не
учитывается, так как расположено после точки). Следовательно, в данном
случае программа должна вывести два символа, разделенных пробелом: 
I 3
"""
import sys
save_stdin = sys.stdin
sys.stdin = open("in/2.in")

import string
s = sys.stdin.read().split('.')[0].upper()
cnt = {}
for c in s:
    if c in string.ascii_uppercase:
        cnt[c] = cnt.get(c,0) + 1
cnt = sorted(cnt.items(), key = lambda x: x[1], reverse = True)
mostFr = sorted([x for x in cnt if x[1] == cnt[0][1]])
print(mostFr[0][0], mostFr[0][1])

sys.stdin = save_stdin