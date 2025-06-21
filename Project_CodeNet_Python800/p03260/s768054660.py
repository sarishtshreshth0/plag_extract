a, b = [int(i) for i in input().split(' ')]
x = a*b
b = 'No'
for i in range(1,4):
    if not x*i %2==0:
        b='Yes'

print(b)