A,B,C,D = map(int, input().split())


if (C > A and C > B) or (A > C and A  >D):
    time =0
else:
    if A < C: # Bの方があとに押した場合
        if B < D:
            time = B-C
        else:
            time = D-C
    else:
        if B<D:
            time = B-A
        else:
            time = D-A
print(time)