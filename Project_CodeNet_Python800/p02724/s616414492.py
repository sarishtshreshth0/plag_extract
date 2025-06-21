# -*= coding: utf-8 -*-
X = int(input())

score = 0

quotient_500 = X // 500
score += quotient_500 * 1000

remainder_500 = X % 500

quotient_5 = remainder_500 // 5
score += quotient_5 * 5

print(score)