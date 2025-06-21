n, m = map(int, input().split())
import heapq

Work = []
for i in range(n):
    Work.append(list(map(int, input().split())))
Work.sort(key=lambda x: (x[0], x[1]), reverse=True)
#print(Work)

total = 0
job_stock = []
#-1をかけた値を格納
heapq.heapify(job_stock)
for day in range(m, -1, -1):
    allowed_delay = m - day
    try:
        while Work[-1][0] <= allowed_delay:
            delay, money = Work.pop()
            heapq.heappush(job_stock, -money)
    except:
        pass
    if len(job_stock) >= 1:
        job_today = -heapq.heappop(job_stock)
        total += job_today
print(total)