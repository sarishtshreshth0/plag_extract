N=int(input())
ans=set()
def saiki(A):
    if len(A)>0:
        B="".join(A)
        count=set(A)
        #print(count)
        if eval(B)<=N:
            if len(count)==3:
                ans.add(B)
        else:
            return
    for i in [3,5,7]:
        A.append(str(i))
        saiki(A)
        A.pop()
saiki([])
print(len(ans))
