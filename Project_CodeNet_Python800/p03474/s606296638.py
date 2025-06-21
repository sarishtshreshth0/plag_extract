# -*- coding: utf-8 -*-

import re

A, B = map(int, input().split())
S = str(input())

text = '[0-9]{' + str(A) + '}-[0-9]{' + str(B) + '}'
pattern = re.compile(text)
matchobj = pattern.match(S)

if matchobj:    
    print('Yes')
else:
    print('No')