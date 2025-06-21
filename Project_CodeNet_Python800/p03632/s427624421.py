a_beg, a_end, b_beg, b_end = map(int, input().split())

beg = max(a_beg, b_beg)
end = min(a_end, b_end)

ans = max(0, end - beg)

print(ans)