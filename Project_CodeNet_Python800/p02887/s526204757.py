from sys import stdin,stdout

if __name__=="__main__":

    n=int(stdin.readline())

    s=str(input())

    l=s[0]
    cnt=1

    for i in range(1,len(s)):
        if(s[i]!=l):
            cnt+=1
            l=s[i]

    stdout.write(str(cnt)+"\n")
