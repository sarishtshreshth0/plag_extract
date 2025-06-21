import math

ceil = math.ceil

def main():
    N = int(input())
    ans = [0]*N
    for i in range(N-1):
        C, S, F = map(int, input().split())
        ans[i] = S + C
        for j in range(i):
            nxt = ceil((ans[j]-S)/F)
            ans[j] = max(0, nxt)*F + S + C
    
    for a in ans:
        print(a)

if __name__ == "__main__":
    main()
