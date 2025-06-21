X = int(input())
ans = int(X/500) * 1000 + int((X - int(X/500)*500)/5)*5
print(ans)