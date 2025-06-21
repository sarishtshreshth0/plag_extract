def main():
    N = int(input())
    red = sorted([tuple(map(int, input().split())) for _ in range(N)], key = lambda x:(-x[1], x[0]))
    blue = sorted([tuple(map(int, input().split())) for _ in range(N)])

    available = [True] * N

    ans = 0
    for bx, by in blue:
        for i, (rx, ry) in enumerate(red):
            if bx > rx and by > ry and available[i]:
                ans += 1
                available[i] = False
                break
    print(ans)
    
if __name__ == "__main__":
    main()