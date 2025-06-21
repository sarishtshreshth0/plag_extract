def resolve():
  N, A, B= map(int, input().split(" "))
  S = list(input())

  sum_of_successful_candidate = 0
  sum_of_successful_b = 0

  for i, s in enumerate(S):
    if sum_of_successful_candidate >= A + B:
      for _ in range(N-i):
        print("No")
      return True

    if s == "a":
      sum_of_successful_candidate += 1
      print("Yes")
    elif s == "b" and sum_of_successful_b < B:
      sum_of_successful_candidate += 1
      sum_of_successful_b += 1
      print("Yes")
    else:
      print("No")

  return True


if __name__ == "__main__":
  resolve()