"""Boot-camp-for-Beginners_Easy006_B_Bishop_25-August-2020.py"""

H, W = (map(int, input().split()))
if(H == 1 or W == 1):
    print(1)
else:
    if (H*W) % 2 == 0:
        print(int(H*W/2))
    else:
        print(int(H*W/2)+1)
