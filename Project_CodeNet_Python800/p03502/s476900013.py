def main():
    N = int(input())
    FN = 0
    res = N
    while res >0:
        FN = FN + res%10
        res = res//10
    if N%FN == 0:
        print('Yes')
    else:
        print('No')
    return
main()