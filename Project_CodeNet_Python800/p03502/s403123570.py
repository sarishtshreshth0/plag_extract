N = int(input())

def digit_sum(n):
    a = 0
    s = str(n)
    for digit in s:
        a += int(digit)
    return a

print(['No','Yes'][N % digit_sum(N) == 0])