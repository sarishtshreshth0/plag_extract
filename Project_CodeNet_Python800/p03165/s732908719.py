def main():
    s = input()
    t = input()
    dp = [[0] * (len(t)+1) for _ in range(len(s)+1)]
    for i,x in enumerate(s):
        for j,y in enumerate(t):
            if x == y:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] =  max(dp[i][j+1], dp[i+1][j])

    ans = ''
    i,j = len(s),len(t)
    while (i>0  and j>0):
        if dp[i][j] == dp[i-1][j]:
            i -= 1
        elif dp[i][j] == dp[i][j-1]:
            j -= 1
        else:
            ans += s[i-1]
            i -= 1
            j -= 1
    print(ans[::-1])

if __name__ == '__main__':
    main()