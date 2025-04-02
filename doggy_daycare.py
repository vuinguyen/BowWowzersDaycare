# Doggy Daycare
# This program simulates a doggy daycare system where dogs can be checked in and out.
# It allows the user to add dogs, check them in and out, and view the list of dogs currently checked in.
# The program uses classes to represent the dogs and the daycare system.
## The program also includes exception handling to manage errors and invalid inputs.

class Dog:
    def __init__(self, name, breed, birth_date, weight):
        self.name = name
        self.breed = breed
        self.birth_date = birth_date
        self.weight = weight
        self.parent = None
        self.favorite_activity = None
        self.checked_in = False
        self.check_in_time = None
        self.check_out_time = None
        self.check_in_duration = None

class Daycare:
    def __init__(self):
        self.dogs = []
        self.checked_in_dogs = []

    def add_dog(self, dog):
        self.dogs.append(dog)
        print(f'{dog.name} has been added to the daycare.')

    def check_in(self, dog_name):
        for dog in self.dogs:
            if dog.name == dog_name:
                if not dog.checked_in:
                    dog.checked_in = True
                    dog.check_in_time = '10:00 AM'  # Placeholder for actual time
                    self.checked_in_dogs.append(dog)
                    print(f'{dog.name} has been checked in.')
                else:
                    print(f'{dog.name} is already checked in.')
                return
        print(f'{dog_name} is not in the daycare.')

    def check_out(self, dog_name):
        for dog in self.checked_in_dogs:
            if dog.name == dog_name:
                dog.checked_in = False
                dog.check_out_time = '4:00 PM'  # Placeholder for actual time
                self.checked_in_dogs.remove(dog)
                print(f'{dog.name} has been checked out.')
                return
        print(f'{dog_name} is not checked in.') 

    def view_checked_in_dogs(self):
        if not self.checked_in_dogs:
            print('No dogs are currently checked in.')
        else:   
            print('Checked-in dogs:')
            for dog in self.checked_in_dogs:
                print(f'Name: {dog.name}, Breed: {dog.breed}, Weight: {dog.weight}, Favorite Activity: {dog.favorite_activity}')
                print('----------------------------------------')

    def view_dogs(self):
        if not self.dogs:
            print('No dogs in the daycare.')
        else:
            print('All dogs in the daycare:')
            for dog in self.dogs:
                print(f'Name: {dog.name}, Breed: {dog.breed}, Weight: {dog.weight}, Favorite Activity: {dog.favorite_activity}')
                print('----------------------------------------')

    def view_dog_details(self, dog_name):
        for dog in self.dogs:
            if dog.name == dog_name:
                print(f'Name: {dog.name}, Breed: {dog.breed}, Birth Date: {dog.birth_date}, Weight: {dog.weight}, Favorite Activity: {dog.favorite_activity}')
                print('----------------------------------------')
                return
        print(f'{dog_name} is not in the daycare.')

    def remove_dog(self, dog_name):
        for dog in self.dogs:
            if dog.name == dog_name:
                self.dogs.remove(dog)
                print(f'{dog.name} has been removed from the daycare.')
                return
        print(f'{dog_name} is not in the daycare.')

    def update_dog_details(self, dog_name, breed=None, birth_date=None, weight=None, favorite_activity=None):
        for dog in self.dogs:
            if dog.name == dog_name:
                if breed:
                    dog.breed = breed
                if birth_date:
                    dog.birth_date = birth_date
                if weight:
                    dog.weight = weight
                if favorite_activity:
                    dog.favorite_activity = favorite_activity
                print(f'{dog.name}\'s details have been updated.')
                return
        print(f'{dog_name} is not in the daycare.')