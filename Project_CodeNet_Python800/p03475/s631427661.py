url = "https://atcoder.jp/contests/abc087/tasks/arc090_a"
import copy
def main():
    n = int(input())
    t = [list(map(int, input().split())) for _ in range(n-1)]
    for i in range(len(t)):
        time = t[i][0] + t[i][1]
        for j in range(i+1, len(t)):
            st = t[j]
            if time <= st[1]:
                time = st[1]
            elif time % st[2] == 0:
                pass
            else:
                time += st[2] - (time % (st[2]))
            time += st[0]
        print(time)
    print(0)



if __name__ == '__main__':
    main()


