from collections import deque
n = int(input())

d = deque()
dic = {}
dic_l = {}

for i in range(n-1):
    a,b = map(int,input().split())

    if(a in dic):
        dic[a].append(b)
    else:
        dic[a] = [b]
    
    if(b in dic):
        dic[b].append(a)
    else:
        dic[b] = [a]
    
    l = max(a,b)
    s = min(a,b)
    dic_l[s,l] = i


#print(dic_l)
mx = 0
for k in dic:
    mx = max(mx,len(dic[k]))

#print("mx",mx)
col = [i+1 for i in range(mx)]
ans = [0 for _ in range(n-1)]
seen = {1}

cnt = 0
tmp = deque()
for i in dic[1]:
    if not(i in seen):
        d.append(i)
        seen.add(i)
        tmp.append(1)
        tmp.append(i)

    load_key = (1,i)
    l_num = dic_l[load_key]
    ans[l_num] = col[cnt]
    cnt += 1


while d:
    nxt = d.popleft()
    tmp_1 = tmp.popleft()
    tmp_2 = tmp.popleft()
    ng = (tmp_1,tmp_2)
    #print(ng)
    ng_col = ans[dic_l[ng]]
    cnt = 0
    for i in dic[nxt]:
        if not(i in seen):
            d.append(i)
            seen.add(i)
            tmp.append(nxt)
            tmp.append(i)
            l = max(nxt,i)
            s = min(nxt,i)
            load_key = (s,l)
            l_num = dic_l[load_key]
            while cnt+1 == ng_col:
                cnt += 1
            ans[l_num] = col[cnt]
            cnt += 1

print(mx)
for s in ans:
    print(s)
