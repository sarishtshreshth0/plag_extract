import collections
import sys
sys.setrecursionlimit(10**6)
dd = collections.defaultdict(int)
def dfs(i,n):
    if(i<=n):
        k = [0,0,0]
        for j in range(len(str(i))):
            if(int(str(i)[j])==3):
                k[0]=1
            if(int(str(i)[j])==5):
                k[1]=1
            if(int(str(i)[j])==7):
                k[2]=1
        if 0 not in k:
            dd[i]=1
        dfs(int(str(i)+"3"),n)
        dfs(int(str(i)+"5"),n)
        dfs(int(str(i)+"7"),n)


def main():
    n = int(input())
    res = 0
    a = [3,5,7]
    for i in a:
        dfs(i,n)
    for key in dd.keys():
        res+=1
    print(res)
    

if __name__ == "__main__":
    main()