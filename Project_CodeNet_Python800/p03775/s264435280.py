n=int(input())

ans_list=[]
a_max=int(n**(1/2))+1
for a in range(1,a_max):
    if n%a==0:
        
        b=n//a
        num_a=len(list(str(a)))
        num_b=len(list(str(b)))
        
        ans_list.append(max(num_a,num_b))
    
print(min(ans_list))
    
