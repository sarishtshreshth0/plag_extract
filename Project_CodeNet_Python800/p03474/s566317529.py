a,b=map(int,input().split())
num_list=[i for i in range(10)]
num_list=[str(i) for i in num_list]
s=input()
if s[a]=="-":
    s=s[:a]+s[a+1:]
    for i in range(len(s)):
        if s[i] not in num_list:
            print("No")
            exit()
    print("Yes")
    exit()
print("No")