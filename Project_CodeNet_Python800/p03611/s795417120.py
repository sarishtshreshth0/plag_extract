from collections import Counter

def main():
    n = int(input())
    a = Counter(map(int, input().split()))
    akeys = a.keys()
    mx = max(akeys)
    cnt = 0
    for i in akeys:
        c = a[i]
        if i+1 in akeys:
            c += a[i+1]
        if i+2 in akeys:
            c += a[i+2]
        cnt = max(cnt, c)
    print(cnt)
    
if __name__ == "__main__":
    main()