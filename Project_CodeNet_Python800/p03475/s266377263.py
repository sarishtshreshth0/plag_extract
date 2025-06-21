def solve(n, t_list):

    ans = [t[1] for t in t_list]
    ans.append(0)
    for i, t in enumerate(t_list):
        for j in range(i+1):
            if ans[j] < t[1]:
                ans[j] += t[0]+(t[1] - ans[j])
            else:
                if ans[j] % t[2] == 0:
                    ans[j] += t[0]
                else:
                    ans[j] += t[0] + (ans[j] // t[2] + 1)*t[2] - ans[j]

    for i in ans:
        print(i)

if __name__ == "__main__":
    n = int(input())
    t_list = [[int(j) for j in input().split()] for i in range(n-1)]
    solve(n, t_list)
