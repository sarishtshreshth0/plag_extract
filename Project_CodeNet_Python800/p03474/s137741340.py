

def main():
    A, B = map(int, input().split())
    s = input()
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    flag = True
    if len(s) == A + B + 1:
        if s[A] != '-':
            flag = False
        for a in s[:A]:
            if a not in numbers:
                flag = False
        for b in s[A+1:]:
            if b not in numbers:
                flag = False
    else:
        flag = False
    
    if flag:
        print("Yes")
    else:
        print("No")
        

if __name__ == "__main__":
    main()