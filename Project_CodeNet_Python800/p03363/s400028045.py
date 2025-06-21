N = int(input())
A_list = list(map(int, input().split()))

sum_list = [0]
for a in A_list:
    sum_list.append(sum_list[-1] + a)

sum_list.sort()
cnt = 0
same_cnt = 0
prev = 10**9
for v in sum_list:
    same_cnt = 0 if prev != v else (same_cnt + 1)
    cnt += same_cnt
    prev = v

print(cnt)