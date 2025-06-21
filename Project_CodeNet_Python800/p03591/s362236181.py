
def main():
    S = input()
    if len(S)<=3:
        print("No")
        exit()
    else:
        S = S[0:4]
        if S == "YAKI":
            print("Yes")
        else:
            print("No")
if __name__ == "__main__":
    main()