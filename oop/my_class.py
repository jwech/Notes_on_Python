# Create Dog Class
class Dog:
    '''Simulate dog'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def sit(self):
        '''Simulate when ordered to sit'''
        print(self.name.title() + ' is now sitting.')
    
    def roll_over(self):
        '''Simulate when ordered to roll over'''
        print(self.name.title() + " rolled over.")

my_dog = Dog('willie', 6)
# access attributes with .
print("My dog's name is " + my_dog.name.title()) 
print("My dog is " + str(my_dog.age) + " years old.")
# call methods
my_dog.sit()
my_dog.roll_over()

class Restaurant:
    '''Simulate Restaurant'''
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type

    def describe_restaurant(self):
        print('Name:', self.name)
        print('Type:', self.type)

    def open_restaurant(self):
        print(self.name + 'is open now.')

r = Restaurant('pizza', 'snack')
r.describe_restaurant()
r.open_restaurant()

class User:
    '''User class includes infos of users'''
    def __init__(self, first_name, last_name):
        self.first = first_name
        self.last = last_name
    
    def describe_user(self):
        '''print infos of user'''
        print('First name:', self.first.title())
        print('Last name:', self.last.title())
    
    def greet_user(self):
        '''greet user'''
        print('Hello,', self.first.title(), self.last.title())

u = User('joe', 'wei')
u.describe_user()
u.greet_user()
