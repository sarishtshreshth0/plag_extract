input()
a = list(map(int,input().split()))
former = []
latter = []
difference = 1000
for i in range(1,len(a)):
    former = []
    latter = []
    for j in range(len(a)):
        if j <= i:
            former.append(a[j])
        else:
            latter.append(a[j])
    if abs(sum(former) - sum(latter)) < difference:
        difference = abs(sum(former) - sum(latter))
print(difference)