a,b=map(int,input().split())
s=input()
lst=["1","2","3","4","5","6","7","8","9","0"]
if len(s)==a+b+1:
    if s[a]=="-":
        switch=1
        for i in range(a+b+1):
            if i!=a:
                if not s[i] in lst:
                    switch=0
                    break
        if switch==1:
            print("Yes")
            exit()
        
print("No")