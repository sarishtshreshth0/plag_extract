H, W = map(int, input().split())

H_ = H % 2
W_ = W % 2

if H  == 1 or W == 1:
    print(1)

elif H_ == 0:
    print(str(round(H/2*W//1)))

elif H_ == 1:
    h = H // 2 + 1
    h_ = H // 2
    if W_ == 0:
        print(str(round((h + h_)*W/2)))

    elif W_ == 1:
        w = W // 2+1
        w_ = W // 2
        print(str(round(h * w + h_ * w_)))



