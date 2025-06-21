n = int(input())
s = input()

t = s
while "()" in t:
    t = t.replace("()", "")

a = t.count(")"); b = t.count("(")

print("(" * a + s + ")" * b)
