# -*- coding: utf-8 -*-

N = int(input().strip())
ab_list = [list(map(int, input().rstrip().split())) for i in range(N)]
cd_list = [list(map(int, input().rstrip().split())) for i in range(N)]
#-----

cd_list.sort()
cnt = 0

for b_x, b_y in cd_list:
    tmp_red = [ [r_x, r_y] for r_x, r_y in ab_list if (r_x < b_x) and (r_y < b_y) ]
    
    if tmp_red:
        tmp_red.sort(key= lambda x: x[1])
        
        cnt += 1
        ab_list.remove( tmp_red[-1] )

print(cnt)
