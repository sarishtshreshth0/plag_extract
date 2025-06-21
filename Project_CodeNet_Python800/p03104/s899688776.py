a, b = map(int, input().split())

res = 0
i = 0
two = 2
while 1 << i <= b:
    mod_a, mod_b = a % two, b % two
    tmp_a, tmp_b = a - mod_a + two, b - mod_b

    cnt = ((tmp_b - tmp_a) // two) * (two // 2)
    cnt += min(two - mod_a, two // 2)
    cnt += max(mod_b - two // 2 + 1, 0)
    
    if cnt % 2 == 1:
        res += two // 2
    
    two *= 2
    i += 1

print(res)