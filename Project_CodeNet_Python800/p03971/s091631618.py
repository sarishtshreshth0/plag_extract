def solve1(n, a, b, s):
    ans = ["No" for i in range(len(s))]

    #print("|     i|s[i]|     a|     b|ans[i]|")
    #print("----------------------------------")

    for i in range(len(s)):
        if s[i] == "a":
            if a > 0:
                ans[i] = "Yes"
                a -= 1
            elif b > 0:
                ans[i] = "Yes"
                b -= 1
        elif s[i] == "b":
            if b > 0:
                ans[i] = "Yes"
                b -= 1

        #print(f"|{i:6d}|{s[i]:4s}|{a:6d}|{b:6d}|{ans[i]:6s}|")

    return ans


n, a, b = map(int, input().split(" "))
s = input()

print("\n".join(solve1(n, a, b, s)))
