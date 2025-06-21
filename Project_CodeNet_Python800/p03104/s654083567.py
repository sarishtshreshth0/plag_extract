a,b = map(int,input().split())

mid_xor = 0
if a%2 == 0 and b%2 == 1:
    even_cnt = (b-a+1)//2
    if even_cnt%2 == 0:
        mid_xor = 0
    else:
        mid_xor = 1
    print(mid_xor)

elif a%2 == 1 and b%2 == 0:
    even_cnt = (b-1-(a+1)+1)//2
    if even_cnt%2 == 0:
        mid_xor = 0
    else:
        mid_xor = 1
    print(a^mid_xor^b)

elif a%2 == 0 and b%2 == 0:
    even_cnt = (b-a)//2
    if even_cnt%2 == 0:
        mid_xor = 0
    else:
        mid_xor = 1
    print(mid_xor^b)
    
elif a%2 == 1 and b%2 == 1:
    even_cnt = (b-a)//2
    if even_cnt%2 == 0:
        mid_xor = 0
    else:
        mid_xor = 1
    print(a^mid_xor)