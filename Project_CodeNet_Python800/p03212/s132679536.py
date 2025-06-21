def dfs(A):
    x ="".join(A)
    if 3 <=len(A) :
        
        if int(x) <=N :
            if x.count("3") >=1 and x.count("5") >=1 and x.count("7") >=1:
                c.append(int(x))
    if len(x) ==len(str(N)): #終了条件
        return

    for i in ["3","5","7"] :
        A.append(i)
        dfs(A)
        A.pop()
 
N = int(input())
c =[]
a =dfs([])
print(len(c))