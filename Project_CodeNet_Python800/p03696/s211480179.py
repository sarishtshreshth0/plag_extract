def main():
    N = int(input())
    S = input()

    count = 0
    for i in range(N-1, -1, -1):
        if S[i] == ")":
            count +=1
        else:
            if count:
                count -= 1
            else:
                S += ")"
    S = "("*count + S
    print(S)

if __name__ == "__main__":
    main()
