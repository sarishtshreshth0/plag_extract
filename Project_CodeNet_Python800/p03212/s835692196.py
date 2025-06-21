import queue

n=int(input())

q=queue.Queue()

q.put(3)
q.put(5)
q.put(7)

c=0
num=q.get()
while num<=n:
    if "3" in str(num) and "5" in str(num) and "7" in str(num):
        c+=1
    q.put(num*10+3)
    q.put(num*10+5)
    q.put(num*10+7)
    num=q.get()

print(c)
