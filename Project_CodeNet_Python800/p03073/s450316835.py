s=input()
n=len(s)

if n%2==0:
    odd=even=n//2
else:
    even=n//2
    odd=even+1
    
odd_black=0
even_black=0

for i in range(n):
    if i%2==0:
        if s[i]=="0":
            odd_black+=1
    else:
        if s[i]=="0":
            even_black+=1

odd_white=odd-odd_black
even_white=even-even_black

if odd_black<=even_black:
    count=odd_black+even_white
else:
    count=odd_white+even_black

print(count)