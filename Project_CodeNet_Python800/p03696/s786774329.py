n = int(input())
s = input()
ss = s

for i in range(1+n//2):
    ss = ss.replace("()","")

sta = ss.count("(")
end = ss.count(")")

print("("*end + s + ")"*sta)