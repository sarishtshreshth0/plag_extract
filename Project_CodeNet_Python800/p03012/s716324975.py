N = int(input())
W = list(map(int, input().split()))
add=0
ans=list()
for i in W:
    add+=i
    ans.append(abs(add-(sum(W)-add)))
print(min(ans))