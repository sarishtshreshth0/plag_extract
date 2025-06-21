def actual(s):
    N = len(s)
    num_repeat = (N // 2)

    if N % 2 == 0:
        # 偶数の場合 1010... か 0101... に限られる
        valid_pattern1 = '10' * num_repeat
        valid_pattern2 = '01' * num_repeat
    else:
        # 奇数の場合 10101... か 10101... に限られる
        valid_pattern1 = '1' + '01' * num_repeat
        valid_pattern2 = '0' + '10' * num_repeat

    flip_step1 = 0
    flip_step2 = 0

    for bit, v1, v2 in zip(s, valid_pattern1, valid_pattern2):
        flip_step1 += int(bit != v1)
        flip_step2 += int(bit != v2)

    return min(flip_step1, flip_step2)


s = input()
print(actual(s))