'''Read from files'''

filename = 'pi_digits.txt'
# Read all lines
with open(filename) as f:
    contents = f.read()
    print(contents.rstrip())

# Read line by line
with open(filename) as f:
    for line in f:
        print(line.rstrip())

# Create list contains all lines
with open(filename) as f:
    lines = f.readlines()
print(lines)

# Access contents in file
pi_string = ''
for line in lines:
    pi_string += line.strip()
print(pi_string)
print(len(pi_string))

'''Write to files'''
filename = 'programming.txt'
with open(filename, 'w') as f:
    f.write("I love progamming.\n")
    f.write("I love creating new games.\n")

'''Append to files'''
with open(filename, 'a') as f:
    f.write("I also love finding meaning in large datasets.\n")
    f.write("I love creating apps that can run in a browser.\n")