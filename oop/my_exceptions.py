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
    msg = "Sorry, the file " + filename + "does not exist."
    print(msg)