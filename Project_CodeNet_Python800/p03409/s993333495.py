def main():
    n = int(input())
    r = [list(map(int, input().split())) for _ in range(n)]
    b = [list(map(int, input().split())) for _ in range(n)]

    #左から考える
    b.sort(key=lambda x: x[0])
    ans = 0

    for nb in b:
        #残っている青玉の一番左のものと条件を満たすものをサーチする
        r_sorted = [i for i in r if i[0] < nb[0] and i[1] < nb[1]]
        #もし条件を満たすものがるなら
        if r_sorted:
            #その中で一上のものを取り除く
            r_sorted.sort(key=lambda x: x[1], reverse=True)
            r.remove(r_sorted[0])
            ans += 1

    print(ans)

if __name__ == "__main__":
    main()
