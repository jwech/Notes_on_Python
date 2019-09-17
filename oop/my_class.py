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

class Car:
    '''Simulate car class'''
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        # defaul value of attributes
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        '''return full info'''
        long_name = str(self.year) + ' ' + self.make.title() + ' ' + self.model.title()
        return long_name
    
    def read_odometer(self):
        '''read odometer'''
        print('This car has ' + str(self.odometer_reading) + ' miles on it.')
    
    def update_odometer(self, mileage):
        '''update odometer'''
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('You cannot roll back an odomter.')
    
    def increment_odometer(self, mileage):
        '''Increase odometer'''
        self.odometer_reading += mileage

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# revise value of attributes directely
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# revise value of attibutes through methods
my_new_car.update_odometer(30)
my_new_car.read_odometer()

my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name)

my_used_car.update_odometer(23500)
my_used_car.read_odometer()
my_used_car.increment_odometer(100)
my_used_car.read_odometer()

'''Inheritance of classes'''
class ElectricCar(Car):
    '''Eelectric car from Car'''
    def __init__(self, make, model, year):
        # Initialize father class attributes
        super().__init__(make, model, year)
        # Equal to 
        # Car.__init__(self, make, model, year)

        # Son class unique attributes
        # self.battery_size = 70

        self.battery = Battery()
    
    # # Define son methods
    # def describe_battery(self):
    #     '''Print info of battery'''
    #     print('This car has a ' + str(self.battery_size) + '-kwh battery.')
    
    # Over write father methods
    def fill_gas_tank(self):
        '''Electric car has no gas tank'''
        print("This car doesn't need a gas tank.")

class Battery:
    '''Simulate battery'''
    def __init__(self, battery_size=70):
        self.battery_size = battery_size
    
    def describe_battery(self):
        '''Print info of battery'''
        print("This car has a " + str(self.battery_size) + '-kwh battery.')
    
    def get_range(self):
        '''Calculate range left'''
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 80:
            range = 270
        
        msg = "This car can go approximately " + str(range)
        msg += ' miles on a full charge.'
        print(msg)


e = ElectricCar('tesla', 'model 3', 2019)
print(e.get_descriptive_name())
e.battery.describe_battery()
e.battery.get_range()