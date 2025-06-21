# -*- coding: utf-8 -*-
a,b,c,d = map(int, input().split())
start_later = max(a,c)
stop_earlier = min(b,d)
res = stop_earlier - start_later
print(res if res > 0 else 0)
