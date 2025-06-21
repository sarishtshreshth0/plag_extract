n=int(input())
s=[input()]
for i in range(n-1):
    w=input()
    if s[-1][-1]==w[0]:
        if not w in s:
            s.append(w)
            
if len(s)==n:
    print("Yes")
else:
    print("No")