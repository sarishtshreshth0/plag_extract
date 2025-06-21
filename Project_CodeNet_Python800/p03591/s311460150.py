# coding: utf-8
# Your code here!

import re

S = input()

# print(S)

# content = r'hellow python, 123, end.' 
content = S

# pattern = 'hel'
pattern = '^YAKI'

# result = re.match(pattern, content)

# print(result)


if re.match(pattern, content):
    print('Yes')
else:
    print('No')