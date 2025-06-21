N, A, B = map(int, input().split())
S = input()
vec_yn = ["No"] * len(S)
passed = 0
passed_oversea = 0
for i in range(len(S)):
    if S[i]=='a':
        if passed < A+B:
            vec_yn[i] = "Yes"
            passed+=1
        else:
            pass
    elif S[i]=='b':
        if passed < A+B and passed_oversea < B:
            vec_yn[i] = "Yes"
            passed+=1
            passed_oversea+=1
        else:
            pass
    else:
        pass

for i in range(len(S)):
    print(vec_yn[i])
