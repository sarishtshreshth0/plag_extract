import re


def actual(a, b, s):
    pattern = r'\d{' + f'{a}' + r'}-\d{' + f'{b}' + '}'
    
    if re.fullmatch(pattern, s):
        return 'Yes'

    return 'No'

a, b = map(int, input().split())
s = input()

print(actual(a, b, s))