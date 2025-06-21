N = int(input())
A = list(map(int, input().split()))

a_max = max(A)
a_min = min(A)

cnt_dict = {}
for i in range(a_min-1, a_max+2):
    cnt_dict[i] = 0
for i in range(len(A)):
    cnt_dict[A[i]-1] += 1
    cnt_dict[A[i]] += 1
    cnt_dict[A[i]+1] += 1

print(max(cnt_dict.items(), key = lambda x: x[1])[1])
