n = int(input())
iterator = n
while True:
    if iterator % n == 0 and iterator % 2 == 0:
        print(iterator)
        break
    else:
        iterator += n
