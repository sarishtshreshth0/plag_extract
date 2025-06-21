N, M, K = map(int, input().split())
friend = {}
for i in range(M):
    A, B = map(lambda x: x-1, map(int, input().split()))
    if A not in friend:
        friend[A] = []
    if B not in friend:
        friend[B] = []
    friend[A].append(B)
    friend[B].append(A)

block = {}
for i in range(K):
    C, D = map(lambda x: x-1, map(int, input().split()))
    if C not in block:
        block[C] = []
    if D not in block:
        block[D] = []
    block[C].append(D)
    block[D].append(C)

first = {}
for i in range(N):
    if i not in first:
        first[i] = i
        if i in friend:
            queue = []
            queue.extend(friend[i])
            counter = 0
            while counter < len(queue):
                item = queue[counter]
                first[item] = i
                if item in friend:
                    for n in friend[item]:
                        if n not in first:
                            queue.append(n)
                counter += 1

size = {}
for key in first:
    if first[key] not in size:
        size[first[key]] = 1
    else:
        size[first[key]] += 1

for i in range(N):
    if i not in friend:
        print(0)
        continue
    no_friend = 0
    if i in block:
        for b in block[i]:
            if first[b] == first[i]:
                no_friend += 1
    print(size[first[i]] - len(friend[i]) - no_friend - 1)