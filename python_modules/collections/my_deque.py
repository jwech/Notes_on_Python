from collections import deque

'''
collections.deque([iterable[, maxlen]])
deque.append(x) / deque.appendleft(x)
deque.pop() / deque.popleft()
deque.extend(iterable)

'''

d = deque('ghi')
for i in d:
    print(i)
d.append('j')
d.appendleft('f')
print(d)
d.pop()
d.popleft()
print(list(d))
print(list(reversed(d)))
d.extend('jkl')
print(d)

def tail(filename, n=10):
    'Return the last n lines of a file'
    with open(filename) as f:
        return deque(f, n)

lines = ['Use python', 'python is a good','and java is good', 'c is good', 'ruby is good','I love python']
def search(lines, pattern, history=2):
    pre_lines = deque(maxlen=history)
    for li in lines:
        if pattern in li:
            pre_lines.append(li)
            yield li, pre_lines        
for i in search(lines, 'python'):
    print(i)

import itertools
def moving_avg(iterable, n=3):
    it = iter(iterable)
    d = deque(itertools.islice(it, n-1))
    d.appendleft(0)
    s = sum(d)
    print(s)
    for elem in it:
        print(elem)
        s += elem - d.popleft()
        print(s)
        d.append(elem)
        print(s/n)
moving_avg([40, 30, 50, 46, 39, 44])

