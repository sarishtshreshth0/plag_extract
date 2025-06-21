from sys import stdin
def main():
    #入力
    readline=stdin.readline
    n=int(readline())
    ab=[0]*n
    for i in range(n):
        ab[i]=list(map(int,readline().split()))
    cd=[0]*n
    for i in range(n):
        cd[i]=list(map(int,readline().split()))

    ab.sort(key=lambda x:x[1])
    ab.sort(key=lambda x:x[0])
    cd.sort(key=lambda x:x[1],reverse=True)
    cd.sort(key=lambda x:x[0],reverse=True)

    res=0
    m=-1
    for i in range(n):
        c=cd[m][0]
        d=cd[m][1]
        now=-1
        key=-1
        for j in range(len(ab)):
            a=ab[j][0]
            b=ab[j][1]
            if a<c:
                if b<d and now<b:
                    now=b
                    key=j
            else:
                break
        if key>=0:
            res+=1
            ab.pop(key)
            cd.pop(m)
        else:
            m-=1
    print(res)

if __name__=="__main__":
    main()