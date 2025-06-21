N, A, B = map(int, input().split())
S = input()
student_pass = A + B
abroad_student_pass = B
passed_students = 0
passed_students_abroad = 0


for status in S:
  if status == 'c':
    print('No')
  elif status == 'a':
    if passed_students < student_pass:
      print('Yes')
      passed_students += 1
    else:
      print('No')
  elif status == 'b':
    if passed_students < student_pass and passed_students_abroad < abroad_student_pass:
      print('Yes')
      passed_students += 1
      passed_students_abroad += 1
    else:
      print('No')