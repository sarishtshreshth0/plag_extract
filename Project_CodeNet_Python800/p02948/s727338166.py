
from collections import defaultdict
import heapq


def submit():
    n, m = map(int, input().split())
    jobs = defaultdict(list)
    job_q = []

    # jobs[a] : a日後に報酬をもらえる仕事についてヒープ
    for _ in range(n):
        a, b = map(int, input().split())
        heapq.heappush(jobs[a], -b)

    # 1日前~m日前について、えらぶべきjobを選択する
    ans = 0
    for i in range(1, m + 1):
        # print("jobs", jobs)
        # print("jobq", job_q)
        if jobs[i]: # 今日期限の仕事について、最大報酬の仕事を候補に入れる
            heapq.heappush(job_q, (heapq.heappop(jobs[i]), i))
        
        # 仕事の候補がある
        if job_q:
            pay, day = heapq.heappop(job_q)
            ans -= pay
            if jobs[day]: # 仕事をしたことにした日の次のjobを候補に追加
                heapq.heappush(job_q, (heapq.heappop(jobs[day]), day))
    print(ans)
            
            
submit()