def main():
    n,k = map(int, input().split())

    c = 0
    while True:
        if n >= k ** c:
            c += 1
        else:
            break
    
    print(c)
    return
main()
