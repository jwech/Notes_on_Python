''' Unpack sequence values to multiple variables'''

# Unpack directly to multiple variables
p = (4, 5)
x, y = p
print(x)
print(y)

data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data
print(name)
print(shares)
print(price)
print(date)

s = 'Hello'
a, b, c, d, e = s
print(a)
print(b)
print(c)

# Unpack part of the sequence
data = ['ACME', 50, 91.1, (2012, 12, 21)]
_, shares, price, _ = data
print(shares)
print(price)

''' Use * operation to unpack'''
def drop_first_last(grades):
    first, *middle, last = grades
    return avg(middle)

# Uncertain quantity of values
record = ('Dave', 'dave@example.com', '773-112', '313-314')
name, email, *phone_numbers = record
print(name)
print(email)
print(phone_numbers)

*trailling, current = [10, 8, 7, 1, 9, 5, 10, 3]
print(trailling)
print(current)

# Use * operation for extendable tuples
records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4)
]
def do_foo(x, y):
    print('foo', x, y)

def do_bar(s):
    print('bar', s)

for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    if tag == 'bar':
        do_bar(*args)

# Use * operation for strings
line =  'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print(uname)
print(homedir)
print(sh)

# Ignore some data
record = ('ACME', 50 ,123.45, (12, 18, 2012))
name, *_, (*_, year) = record
print(name)
print(year)

items = [1, 10, 7, 4, 5, 9]
def sum(items):
    head, *tails = items
    return head + sum(tails) if tails else head
print(sum(items))