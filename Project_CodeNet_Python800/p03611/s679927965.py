from collections import Counter
n = int(input())
a = list(map(int,input().split()))
a_n = []

for i in range(n):
    a_n.append(a[i])
    a_n.append(a[i]-1)
    a_n.append(a[i]+1)


counter=Counter(a_n)

print(a_n.count(counter.most_common()[0][0]))



                
            

            
