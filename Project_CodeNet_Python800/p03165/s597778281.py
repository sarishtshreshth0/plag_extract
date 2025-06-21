from collections import deque

def mymax(a:int, b:int, c:int):
    if a > b:
        if c > a:
            return c
        else:
            return a
    else:
        if c > b:
            return c
        else:
            return b


def main():
    s = input()
    t = input()
    lens = len(s)
    lent = len(t)
    dp = [[0] * (lent+1) for _ in range(lens+1)]


    for i in range(1, lens + 1):
        for j in range(1, lent + 1):
            dp[i][j] = mymax(
                dp[i-1][j-1] + (s[i-1] == t[j-1]),
                dp[i-1][j],
                dp[i][j-1]
            )
    
    string = deque([])
    i = lens; j = lent
    for _ in range(lens+lent+1):
        if s[i-1] == t[j-1]:
            string.appendleft(s[i-1])
            i -= 1
            j -= 1
        else:
            if dp[i-1][j] > dp[i][j-1]:
                i -= 1
            else:
                j -= 1
        if i <= 0 or j <= 0:
            break
    print(''.join(string))

if __name__ == "__main__":
    main()
