A,B,C = map(int,input().split())
print("Yes" if (A<=C and C<=B) or (A>=C and C>=B) else "No")
