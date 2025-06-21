import sys

def main():

    n,a,b = list(map(int, input().split()))
    s = input()
    yes_a = 0
    yes_b = 0
    
    for i in range(n):
        s_i = s[i]
        if (yes_a+yes_b) < (a+b):
            if s[i] == "a":
                print("Yes")
                yes_a += 1
            if s[i] == "b":
                if yes_b < b:
                    print("Yes")
                    yes_b += 1
                else:
                    print("No")
            if s[i] == "c":
                print("No")
        else:
            print("No")
        
    
if __name__ == "__main__":
    main()