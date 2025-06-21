"""Boot-camp-for-Beginners_Easy003_B_Qualification-simulator_19-August-2020.py"""
N, A, B = map(int, input().split())
S = str(input())

RANK_a = 0
RANK_b = 0

for i in range(N):
    if S[i] == "a":
        if RANK_a+RANK_b < A+B:
            RANK_a += 1
            print("Yes")
        else:
            print("No")
    elif S[i] == "b":

        if RANK_a+RANK_b < A+B:
            if RANK_b < B:
                RANK_b += 1
                print("Yes")
            else:
                print("No")
        else:
            print("No")
    else:
        
        print("No")
