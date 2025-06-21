def r(a): #ランレングス圧縮
    ll,l=[],1
    for i in range(len(a)-1):
        if a[i]==a[i+1]:
            l+=1
        else:
            ll.append(l)
            l=1
    ll.append(l)
    return ll

def cum(a): #累積和
    b,c=[0],0
    for i in range(len(a)):
        c+=a[i]
        b.append(c)
    return b

n=int(input())
print(sum([i*(i-1)//2 for i in r(sorted(cum(list(map(int,input().split())))))]))