
import sys
input = sys.stdin.readline

def main():
    s = input()
    t = input()

    s_len = len(s)
    t_len = len(t)
    dp = [[0]*(t_len + 1) for _ in range(s_len + 1)]

    # 最長共通部分列の長さを求めるDP配列を作る
    for i1 in range(1, s_len + 1):
        for i2 in range(1, t_len + 1):
            if s[i1 - 1] == t[i2 - 1]:
                dp[i1][i2] = dp[i1-1][i2-1] + 1
            else:
                dp[i1][i2] = max(dp[i1-1][i2], dp[i1][i2-1])
    #for k in range(s_len):
    #    print(dp[k])
    #print("--")
    # DP配列から最長共通部分列をもとめる。
    j1 = s_len
    j2 = t_len
    r = ""
    while j1 > 0 and j2 > 0:
        #print(j1, j2)
        if s[j1-1] == t[j2-1]:
            r += s[j1-1]
            j1 -= 1
            j2 -= 1
        elif dp[j1 - 1][j2] == dp[j1][j2]:
            j1 -= 1
        else:
            j2 -= 1
    print(r[::-1])


if __name__ == '__main__':
    main()
