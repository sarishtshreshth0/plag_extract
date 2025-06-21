A,B=map(int,input().split())
k=A%4
AA=A+4-k
l=B%4
BB=B-l
AAA=[]
BBB=[]
for i in range(A,AA):
    AAA+=[i]
for i in range(BB,B+1):
    BBB+=[i]

def henkan(A):
    if len(A)==4 or len(A)==0:
        return 0
    elif len(A)==3:
        return A[0]^A[1]^A[2]
    elif len(A)==2:
        return A[0]^A[1]
    elif len(A)==1:
        return A[0]
print(henkan(AAA)^henkan(BBB))
