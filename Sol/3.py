﻿# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Задача C4-3. 
Решение на языке Python 3.
 Автор: Константин Поляков, 2013
E-mail: kpolyakov@mail.ru
   Web: kpolyakov.spb.ru
-------------------------------------------------
На вход программы подаются произвольные алфавитно-цифровые символы.
Ввод этих символов заканчивается точкой. Требуется написать программу,
которая будет печатать последовательность строчных английских букв
('a' 'b'... 'z') из входной последовательности и частот их повторения.
Печать должна происходить в алфавитном порядке. Например, пусть на
вход подаются следующие символы:
   fhb5kbfshfm.
В этом случае программа должна вывести
   b2
   f3
   h2
   kl
   ml
   s1
"""
import sys
save_stdin = sys.stdin
sys.stdin = open("in/3.in")

import string
s = sys.stdin.read().split('.')[0]
s = [x for x in s if x in string.ascii_lowercase]
cnt = {}
for c in s:
   cnt[c] = cnt.get(c,0) + 1
for x in sorted(cnt.items()):
   print("%s %d" % (x))

sys.stdin = save_stdin