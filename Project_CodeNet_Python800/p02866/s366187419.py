def pow(x,n):
    res = 1
    for _ in range(n):
        res *= x
    return max(1,res)

def main():
    N = int(input())
    lists = [0 for i in range(N+1)]
    temp = list(map(int,input().split()))

    for elem in temp:
        lists[elem] += 1
    
    ans = 1


    if(lists[0] != 1 or temp[0] != 0):
        ans = 0
    else:
        sum = 1
        for i in range(1,N):
            ans *= pow(lists[i-1],lists[i])
            sum += lists[i]
            if(sum == N):
                break
                
            if(lists[i] == 0):
                if(sum != N):
                    ans = 0
                    break
                
    ans %= 998244353
    print(ans)
    

if __name__ == "__main__":
    main()