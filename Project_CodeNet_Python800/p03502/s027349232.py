n=input()
a=[]
for i in range(len(n)):
  a.append(int(n[i]))
print("Yes" if int(n)%sum(a)==0 else "No")
