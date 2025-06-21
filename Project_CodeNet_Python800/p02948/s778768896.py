#-*-coding:utf-8-*-

import heapq

def main2():
    n,m=map(int,input().split())
    jobs_list=[list(map(int,input().split())) for _ in range(n)]
    #breakするタイミングを作るため、Mより大きい値の仕事を作成
    banpei_list=[[i,0] for i in range(1,m+2)]
    #リストの統合
    jobs_list.extend(banpei_list)
    jobs_list=sorted(jobs_list)
    ans=0
    index=0
    que=[]
    while 1:
        day,pay=jobs_list[index]
        #dayがMを超えていればbreak
        if day>m:
            break
        #同じdayのデータが次にもあれば-1倍してheapにpush
        if day==jobs_list[index+1][0]: 
            heapq.heappush(que,-pay)
        #仕事の報酬の最大値を答えに加える
        #前の日のデータからも報酬が良い仕事は選べるようにqueにデータは貯めておく
        else:
            heapq.heappush(que,-pay)
            ans-=heapq.heappop(que)
        index+=1
    print(ans)

if __name__ == "__main__":
    main2()