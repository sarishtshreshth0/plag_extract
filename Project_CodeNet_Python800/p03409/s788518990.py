if __name__ == '__main__':
    n = int(input())
    red = []
    blue = []
    for i in range(n):
        a, b = map(int, input().split())
        red.append((a, b))
    for i in range(n):
        c, d = map(int, input().split())
        blue.append((c, d))
    red.sort(key=lambda x: x[1], reverse=True)
    blue.sort()
    ans = 0
    for i in range(n):
        for j in range(len(red)):
            a, b, c, d = red[j][0], red[j][1], blue[i][0], blue[i][1]
            if a < c and b < d:
                ans += 1
                del red[j]
                break
    print(ans)
