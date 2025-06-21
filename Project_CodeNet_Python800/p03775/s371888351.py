n=int(input())

divisors = []
for i in range(1, int(n**0.5)+1):
    if n % i == 0:
        divisors.append(i)
        if i != n // i:
            divisors.append(n//i)

divisors.sort()
length=len(divisors)
if length == 2:
    A=str(divisors[0])
    B=str(divisors[1])
elif length%2 == 0:
    A=str(divisors[length//2-1])
    B=str(divisors[length//2])
else:
    A=str(divisors[length//2])
    B=str(divisors[length//2])

#print(A,B)

ans=max(len(A),len(B))
print(ans)