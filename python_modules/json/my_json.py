# Save data
# JSON: JavaSript Object Notation

# json.dump()
# to save data
import json
nums = [2, 3, 4, 5, 8, 13]
filename = './python_modules/json/numbers.json'
with open(filename, 'w') as f:
    json.dump(nums, f)

# json.load()
# to read data
with open(filename) as f:
    nums = json.load(f)
print(nums)

# Save user's data
root = './python_modules/json/'
username = input('What is your name? ')
filename = 'username.json'
with open(root + filename, 'w') as f:
    json.dump(username, f)
    print("We'll remember you when you come back, " + username.title() + '!')

# Read user's data
with open(root + filename) as f:
    username = json.load(f)
    print("Welcome back, " + username.title() + "!")

# In one file
import json
filename = 'username.json'
try:
    with open(root + filename) as f:
        username = json.load(f)
except FileNotFoundError:
    username = input("What is your name?")
    with open(root + filename, 'w') as f:
        json.dump(username, f)
else:
    print('Welcome back, ' + username + '!')
