N = int(input())
cmin = 1000
for i in range(1,int(N**0.5)+1):
    if N%i==0:
        a = str(i)
        b = str(N//i)
        cmin = min(cmin,max(len(a),len(b)))
print(cmin)