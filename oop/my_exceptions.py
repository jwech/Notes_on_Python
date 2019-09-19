# Use try-except
# Deal with ZeroDivisionError
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input('\nSecond number: ')
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    # Deal with ValueError
    except ValueError:
        print("Please enter numbers.")
    else:
        print(answer)

# Deal with FileNotFoundError
filename = './oop/alice.txt'
try:
    with open(filename) as f:
        contents = f.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
else:
    words = contents.split()
    num_words = len(words)
    print('The file ' + filename + ' has about ' + str(num_words) + ' words.')

# Access multiple files
def count_words(filename):
    # Calculate how many words in a file
    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
        # msg = "Sorry, the file " + filename + " does not exist."
        # print(msg)
        pass # Do nonthing when file not found
    else:
        # Calculate numbers of words
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")

filename = './oop/programming.txt'
count_words(filename)

filenames = ['alice.txt', 'siddhartha.txt', 'pi_digits.txt', 'programming.txt']
for filename in filenames:
    count_words('./oop/' + filename)

while True:
    print('Enter two numbers to add: (enter q to quit.)')
    first_num = input('The first num: ')
    if first_num == 'q':
        break
    second_num = input('The second nm: ')
    try:
        sum = int(first_num) + int(second_num)
        print('The sum of the two numbers are:', str(sum))
    except TypeError:
        print('Please enter numbers.')
    except ValueError:
        print('Please enter numbers!')