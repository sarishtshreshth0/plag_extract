N=int(input())
S=input()

while True:
    x=''
    ans=''
    for i in S:
       if (x==''):
        x=i
        continue
       if x!=i:
        #print("p:",x,i,ans)
        ans+=x
        x=i
        #print("a:",x,i,ans)

    ans+=x
    #print('ans:',ans)
    if ans==S:
        break
    else:
        S=ans
print(len(ans))       