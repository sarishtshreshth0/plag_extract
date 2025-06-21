pos_house = [int(x) for x in input().split()]

if pos_house[0] < pos_house[2] < pos_house[1] or \
    pos_house[0] > pos_house[2] > pos_house[1]:
    print("Yes")
else:
    print("No")