h, w = map(int, input().split())
hd, hm, wd, wm = h // 2, h % 2, w // 2, w % 2
s = hd * wd * 2  + hm * wd + wm * hd + hm * wm
if h == 1 or w == 1:
    s = 1
print(s)
