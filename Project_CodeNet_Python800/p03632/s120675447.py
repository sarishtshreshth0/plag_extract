def main():
    A, B, C, D = map(int,input().split())
    if A <= C:
        if B-C <= 0:
            ans = 0
            return ans
        elif B-C > 0 and B <= D:
            ans = B-C
            return ans
        elif B-C > 0 and B > D:
            ans = D-C
            return ans

    elif A > C and A < D:
        if B <= D:
            ans = B-A
            return ans
        elif B > D:
            ans = D-A
            return ans

    elif A >= D:
        ans = 0
        return ans

print(main()) 
