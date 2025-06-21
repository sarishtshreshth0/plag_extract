import heapq
from collections import deque


def main():
    N, M = list(map(int, input().split(' ')))
    tasks = list()
    for _ in range(N):
        req_day, reward = list(map(int, input().split(' ')))
        latest_start_day = M - req_day
        tasks.append((-reward, latest_start_day))
    # sort by desc order of latest_start_day
    tasks.sort(key=lambda t: t[1], reverse=True)
    tasks = deque(tasks)
    task_que = []
    neg_reward = 0
    for d in range(M, -1, -1):
        while len(tasks) > 0 and tasks[0][1] >= d:
            heapq.heappush(task_que, tasks.popleft())
        if len(task_que) == 0:
            continue
        # do task first with local max reward
        task = heapq.heappop(task_que)
        neg_reward += task[0]
    print(-neg_reward)


if __name__ == '__main__':
    main()
