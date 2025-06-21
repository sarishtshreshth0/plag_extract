from collections import deque
N = int(input())

ans = 0
ls = ['3','5','7']
for x in ls:
    st = deque([])
    flag = False
    st.append((x, flag))
    while st:
        cur, f = st.pop()
        if f:
            ans += 1
        else:
            if '3' in set(list(cur)) and '5' in set(list(cur)) and '7' in set(list(cur)):
                # print(cur)
                f = True
                ans += 1
        for y in ls:
            if int(cur + y) <= N:
                st.append((cur+y, f))
print(ans)