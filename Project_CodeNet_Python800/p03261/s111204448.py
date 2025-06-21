N, *W = open(0).read().split()

is_ok = True

if len(W) != len(set(W)):
    is_ok = False
else:
    for i, w in enumerate(W):
        if i > 0:
            if before_w != w[0]:
                is_ok = False
                break
        
        before_w = w[-1]
    
if is_ok:
    print("Yes")
else:
    print("No")