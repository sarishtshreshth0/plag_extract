def main():
    N = int(input())
    S = input()

    temp = S[0]
    result = 1
    for i in range(1,N):
        if temp != S[i]:
            result += 1
            temp = S[i]

    print(result)

if __name__ == '__main__':
    main()