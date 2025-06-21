n = int(input())
t = input()
lef = 0
rig = 0
cl = 0
cr = 0

for i in range(n):
    if t[i] == ")":
        rig += 1
        if rig > lef+cl:
            cl += 1
    if t[i] == "(":
        lef += 1
lef = 0
rig = 0
for i in reversed(range(n)):
    if t[i] == "(":
        lef += 1
        if lef > rig+cr:
            cr += 1
    if t[i] == ")":
        rig += 1

for i in range(cl):
    print("(",end="")
print(t,end="")
for i in range(cr):
    print(")",end="")