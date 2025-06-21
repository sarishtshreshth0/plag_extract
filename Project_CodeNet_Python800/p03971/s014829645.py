#-*-coding:utf-8-*-
import sys
input=sys.stdin.readline

def main():
    candidates=[]
    n,a,b = map(int,input().split())
    [candidates.append(s) for s in input().rstrip()]
    limit=a+b
    b_counter=1

    for idx in range(1,len(candidates)+1):
        if 'a' in candidates[idx-1] and limit > 0:
            limit-=1
            print("Yes")
        elif 'b' in candidates[idx-1] and limit > 0 and b_counter <= b:
            b_counter+=1
            limit-=1
            print("Yes")
        else:
            print("No")
    
if __name__=="__main__":
    main()