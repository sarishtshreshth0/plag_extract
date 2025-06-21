n=int(input())
a=[]
b=[]
i=1
while i*i<=n+1:
    if n%i==0:
        a.append(i)
        b.append(n//i)
    i+=1
print(max((len(list(str(a[-1])))),len(list(str(b[-1])))))
