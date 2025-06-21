def main():
    from sys import stdin
    def input():
        return stdin.readline().strip()
    
    n = int(input())
    red = [tuple(map(int, input().split())) for _ in range(n)]
    blue = [tuple(map(int, input().split())) for _ in range(n)]

    red.sort()
    blue.sort()

    now = 0
    for i in blue:
        while now < len(red) and red[now] < i:
            now += 1
        
        l = red[:now]
        if l == []:
            continue

        l = sorted(l, key=lambda x: x[1])
        for j in range(len(l)-1, -1, -1):
            if l[j][1] < i[1]:
                red.remove(l[j])
                now -= 1
                break

    print(n - len(red))

main()