n = int(input())
m = []
for i in range(n):
    m.append(input())
    
if len(set(m)) != len(m):
    print("No")
    exit()

for j in range(n-1):
    if m[j][-1] != m[j+1][0]:
        print("No")
        exit()
print("Yes")