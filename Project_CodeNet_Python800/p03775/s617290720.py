import math

# 与えられた数値の桁数と桁値の総和を計算する.
def calc_digit_sum(num):
    digits = sums = 0
    while num > 0:
        digits += 1
        sums += num % 10
        num //= 10
    return digits, sums


n = input()
answer = len(n)

num = int(n)
limit = int(math.sqrt(num)) + 1
for divide in range(1, limit):
    candidate = num // divide
    if candidate * divide == num:
        digit1 = len(str(divide))
        digit2 = len(str(candidate))
        answer = min(answer, max(digit1, digit2))

print(answer)

