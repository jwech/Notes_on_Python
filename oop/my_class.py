class Restaurant:
    '''Simulate Restaurant'''
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type

    def describe_restaurant(self):
        print('Name:', self.Name)
        print('Type:', self.type)

    def open_restaurant(self):
        print(self.name + 'is open now.')

r = Restaurant('pizza', 'snack')
r.describe_restaurant()
r.open_restaurant()
