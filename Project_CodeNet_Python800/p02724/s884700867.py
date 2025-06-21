x = int(input())//5 * 5
ans = int((x/500)) * 1000
x -= ans/2
ans += int(x/5)*5
print(ans)
