import collections

N = int(input())
A_s = list(map(int, input().split()))

CNT_A = collections.Counter(A_s).most_common()

ans_list = []

if (len(CNT_A) >= 3):
    CNT_A.sort()

    for i in range(len(CNT_A) - 2):
        val = CNT_A[i][0]
        next_val = CNT_A[i + 1][0]
        nnnn_val = CNT_A[i + 2][0]
        
        
        if (abs(val - next_val) <= 2):
            cnt = CNT_A[i][1] + CNT_A[i + 1][1]
            if (abs(val - nnnn_val) <= 2):
                cnt += CNT_A[i + 2][1]
                
        else:
            cnt = CNT_A[i][1]
        
        ans_list.append(cnt)
    
    ans = max(ans_list)

elif (len(CNT_A) == 2):
    val = CNT_A[0][0]
    n_val = CNT_A[1][0]
    
    if (abs(val - n_val) <= 2):
        ans = CNT_A[0][1] + CNT_A[1][1]
    else:
        ans = CNT_A[0][1]
    
else:
    ans=CNT_A[0][1]

print(ans)