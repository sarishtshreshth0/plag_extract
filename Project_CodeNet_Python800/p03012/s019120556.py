n=int(input())
w_list=[int(i) for i in input().split()]

sa_list=[]
for i in range(n):
    sa_list.append(abs(sum(w_list[:i+1])-sum(w_list[i+1:])))
    
print(min(sa_list))