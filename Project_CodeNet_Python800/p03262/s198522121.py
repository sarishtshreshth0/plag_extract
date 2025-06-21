N,X=map(int,input().split())
x=input().split()
x_s=[int(a) for a in x]

x_s.append(X)

list_s=sorted(x_s)

numbers=[]

for n in range(1,N+1):
    number=list_s[n]-list_s[n-1]
    numbers.append(number)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

number=numbers[0]
for n in range(len(numbers)):
    number=gcd(number,numbers[n])

print(number)
