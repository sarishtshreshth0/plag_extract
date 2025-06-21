def main():
    n = int(input())
    s = input()
    ans = 0
    for i in range(n):
        if i == 0:
            ans += 1
            mae = s[i]
        else:
            if s[i] != mae:
                ans += 1
                mae = s[i]
    print(ans)


    
if __name__ == "__main__":
    main()
