def main():
    a, b = map(int, input().split())
    # xorの累積を調べると周期性が4である余りをrとすると以下のようになる
    # r	累積XOR
    # 0	N 
    # 1	1 
    # 2	N+1
    # 3	0
    def cumxor(n):
        if n % 4 == 0:
            return n
        elif n % 4 == 1:
            return 1
        elif n % 4 == 2:
            return n+1
        else:
            return 0
    
    # aからbまでのxorはa-1までのxorと、bまでのxorになるので
    ans = cumxor(a-1) ^ cumxor(b)        
    print(ans)

if __name__ == '__main__':
    main()