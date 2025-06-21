string1 = input()
string2 = input()

dp = [[0 for i in range(len(string1) + 1)] for j in range(len(string2) + 1)]
substring = ""
for i in range(len(string2) + 1):
    for j in range(len(string1) + 1):
        if i == 0 or j == 0:
            dp[i][j] = 0
        elif string2[i - 1] == string1[j - 1]:
            dp[i][j] = 1 + dp[i - 1][j - 1]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

def recon(dp, string1, string2):
    string = ""
    i, j = len(dp) - 1, len(dp[0]) - 1
    while i != 0 and j != 0:
        if dp[i][j] > max(dp[i - 1][j], dp[i][j - 1]):
            string += string2[i - 1]
            i -= 1
            j -= 1
        else:
            if dp[i - 1][j] > dp[i][j - 1]:
                i -= 1
            else:
                j -= 1

    return string

print(recon(dp, string1, string2)[::-1])