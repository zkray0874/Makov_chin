from collections import deque
d = deque('ghi')
print(d)
for i in d:
    print(i.upper())

d.append('j')
d.appendleft('f')
print(d)
print(d.pop())
r = deque(reversed(d))
print(r)
