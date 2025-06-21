A,B,C=map(int, input().split())
print("YNeos"[not(A<=C<=B or B<=C<=A)::2])