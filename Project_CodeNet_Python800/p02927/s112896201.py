import heapq
from sys import stdin
input = stdin.readline

#入力
# s = input()[0:-1]
# n = int(input())
m,d = map(int, input().split())
# a = list(map(int,input().split()))
# a = [int(input()) for i in range()]


# ab=[]
# for i in range():
#     a,b = map(int, input().split())
#     ab.append([a,b])


     
def main():
    ans = 0
    for i in range(1,m+1):
        for j in range(20,d+1):
            d10 = j//10
            d1 = j%10
            if d10 ==1 or d1 ==1:
                continue
            if d10*d1 == i:
                ans+=1
    print(ans)
    
    

if __name__ == '__main__':
    main()