import sys
n,m=map(int,input().split())
x=list(map(int,input().split()))

if n>=m:
    print(0)
    sys.exit()

def quicksort(a, left: int, right: int):
    #a[left]〜a[right]をクイックソート
    pl=left
    pr=right
    pivot= a[(left +right)//2]

    #print(f'a[{left}]~a[{right}] : ', *a[left : right +1])

    while pl<=pr:
        while a[pl] <pivot: pl+=1
        while a[pr] >pivot: pr-=1
        if pl <= pr:
            a[pl], a[pr]= a[pr], a[pl]
            pl+=1
            pr-=1

    if left < pr: quicksort(a, left, pr)
    if pl < right: quicksort(a, pl, right)

def quick_sort(a):
    quicksort(a, 0, len(a)-1)

quick_sort(x)
dis_list=[0]*(m-1)
dis_sm=0
for i in range(m-1):
    dis=x[i+1]-x[i]
    dis_list[i]=dis
    dis_sm+=dis

quick_sort(dis_list)
for i in range(n-1):
    dis_sm-=dis_list[-(i+1)]

print(dis_sm)
