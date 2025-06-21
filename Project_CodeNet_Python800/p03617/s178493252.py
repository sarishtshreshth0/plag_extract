a, b, c, d = map(int, input().split())
num = int(input())
 
if num % 2 == 0:
    Min = min(num*a*4, num*b*2, num*c, num//2*d)
else:
    Min = min((num-1)*a*4, (num-1)*b*2, (num-1)*c, num//2*d) + min(4*a, 2*b, c)
print(Min)