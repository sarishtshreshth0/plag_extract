N = int(input())
W = [input() for _ in range(N)]

result = 'Yes'
if len(set(W)) != len(W):
    result = 'No'
else:    
    for i in range(1,N):
        if W[i][0] != W[i-1][-1]:
            result = 'No'
            break 
print(result)