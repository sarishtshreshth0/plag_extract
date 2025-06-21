n = int(input())
num = n
total_num = 0

while num != 0:
    total_num += num % 10
    num = num // 10

if n % total_num == 0:
    print('Yes')
else:
    print('No')