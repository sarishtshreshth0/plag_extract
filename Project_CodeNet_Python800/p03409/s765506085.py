MOD = 10**9 +7
INF = 10**9

def main():
    n = int(input())
    R = [tuple(map(int,input().split())) for _ in range(n)]
    B = [tuple(map(int,input().split())) for _ in range(n)]
    
    B.sort(key = lambda x:x[0])
    R.sort(key = lambda x:x[1],reverse=True)
    done = [1] * n
    
    cnt = 0
    for i in range(n):
        bx,by = B[i]
        for j in range(n):
            if done[j] and R[j][0] < bx and R[j][1] < by:
                cnt += 1
                done[j] = 0
                break
    
    print(cnt)
if __name__=='__main__':
    main()