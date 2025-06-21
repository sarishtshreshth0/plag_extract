n = int(input())
score = 100
for i in range(1, 10**6):
    if n % i == 0:
        tmp_score = max(len(str(i)), len(str(n//i)))
        if score > tmp_score:
            score = tmp_score
print(score)
