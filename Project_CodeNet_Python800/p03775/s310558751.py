N=int(input())
print(min(len(str(N//i))for i in range(1,int(N**.5)+1)if N%i<1))
