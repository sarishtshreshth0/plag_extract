n=int(input())
w=[]
w.append(input())
t=1
for i in range(1,n):
    word=input()
    if word in w:
        t=0
        break
    if word[0]!=w[i-1][-1]:
        t=0
        break
    w.append(word)
if t==1:
    print("Yes")
else:
    print("No")