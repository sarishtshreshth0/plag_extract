tmp_lst = input().split()

A, B, C = int(tmp_lst[0]), int(tmp_lst[1]), int(tmp_lst[2])

if A < C and C < B:
    print("Yes")
elif B < C and C < A:
    print("Yes")
else:
    print("No")

