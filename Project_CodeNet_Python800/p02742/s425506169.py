h, w = map(int, input().split())

h_odd = (h+1)//2
h_even = h//2
w_odd = (w+1)//2
w_even = w//2

if h == 1 or w ==1:
    print(1)
else:
    ans = h_odd * w_odd + h_even *w_even
    print(ans)