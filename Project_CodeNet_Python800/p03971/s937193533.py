#!/usr/local/bin/python3

N, A, B = map(int, input().split())
S = input()
cur_rank = 1
world_cur_rank = 1

for s in S:
    pass_cond = cur_rank <= A+B
    if s == 'a' and pass_cond:
        print('Yes')
        cur_rank += 1
    elif s == 'b' and pass_cond and world_cur_rank <= B:
        print('Yes')
        cur_rank += 1
        world_cur_rank += 1
    else:
        print('No')
