def main():
    import math
    n, d = map(int, input().split())
    inlis = []
    for i in range(n):
        inlis.append(list(map(int, input().split())))
    
    ans = 0
    for i in range(n):
        for j in range(n):
            if i < j:
                dist = 0
                for k in range(d):
                    dist += (inlis[i][k] - inlis[j][k])**2
                if (dist ** 0.5).is_integer():
                    ans += 1
    print(ans)
if __name__ == "__main__":
    main()
