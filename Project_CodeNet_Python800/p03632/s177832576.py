s1, f1, s2, f2 = map(int,input().split())
sec = min(f1,f2) - max(s1,s2)
print(sec if sec >= 0 else "0")