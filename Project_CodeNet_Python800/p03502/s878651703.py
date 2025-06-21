def main():
    N = int(input())
    sum_N = 0
    judge_N = N

    while True:
        sum_N += (N%10)
        N = N//10
        if N == 0:
            break

    if (judge_N % sum_N) == 0:
        print('Yes')
    else:
        print('No')

main()
