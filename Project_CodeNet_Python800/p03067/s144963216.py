# Tenka1 Programming Beginner Contest 2019: A – On the Way
a, b, c = [int(s) for s in input().split()]
print('Yes' if a <= c <= b or b <= c <= a else 'No')