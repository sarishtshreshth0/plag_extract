A,B,C =map(int, input().split())
print("Yes") if min(A, B)<C<max(A,B) else print("No")