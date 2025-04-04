# This program is a very simple example of using dictionaries
# to manage dogs in a daycare.

# Initializing an empty dogs dictionary
dogs = {}

# Function to view all dogs in the daycare
def view_dogs(dogs):
    if not dogs:
        print('No dogs in the daycare.')
    else:
        print('All dogs in the daycare:')
        for name, details in dogs.items():
            print(f'Name: {name}, Breed: {details["breed"]}, Birth Date: {details["birth_date"]}, Weight: {details["weight"]}, Favorite Activity: {details["favorite_activity"]}')
            print('----------------------------------------')

# Removing a dog from the daycare
def remove_dog(dogs, dog_name):
    if dog_name in dogs:
        del dogs[dog_name]
        print(f'{dog_name} has been removed from the daycare.')
    else:
        print(f'{dog_name} is not in the daycare.')

# Function to add a dog to the daycare
def add_dog(dogs, name, breed, birth_date, weight, favorite_activity=None):
    if name in dogs:
        print(f'{name} is already in the daycare.')
    else:
        dogs[name] = {
            'breed': breed,
            'birth_date': birth_date,
            'weight': weight,
            'favorite_activity': favorite_activity
        }
        print(f'{name} has been added to the daycare.')

# Function to modify the details of a dog
def modify_dog(dogs, name, breed=None, birth_date=None, weight=None, favorite_activity=None):
    if name in dogs:        
        if breed:
            dogs[name]['breed'] = breed
        if birth_date:
            dogs[name]['birth_date'] = birth_date
        if weight:
            dogs[name]['weight'] = weight
        if favorite_activity:
            dogs[name]['favorite_activity'] = favorite_activity
        print(f'{name} has been modified.')
    else:
        print(f'{name} is not in the daycare.')


# Adding dogs to the daycare
# Each dog is represented as a dictionary with its details
dogs['Rocky'] = {'breed': 'Schnoodle', 'birth_date': '2021-11-01', 'weight': 14, 'favorite_activity': None}
dogs['Bella'] = {'breed': 'Golden Retriever', 'birth_date': '2019-05-15', 'weight': 65, 'favorite_activity': None}
dogs['Daisy'] = {'breed': 'Cairn Terrier', 'birth_date': '2018-07-25', 'weight': 20, 'favorite_activity': None}
dogs['Hashbrown'] = {'breed': 'French Bulldog', 'birth_date': '2016-06-01', 'weight': 30, 'favorite_activity': None}

view_dogs(dogs)

# Modifying the details of a dog
dogs['Rocky']['favorite_activity'] = 'Chasing'
dogs['Bella']['favorite_activity'] = 'Fetching'
dogs['Daisy']['favorite_activity'] = 'Snuggling'
dogs['Hashbrown']['favorite_activity'] = 'Sleeping'

view_dogs(dogs)

remove_dog(dogs, 'Bella')

view_dogs(dogs)

######
# The following is an example of managing dogs in the daycare using arrays
# and lists instead of dictionaries. This is not the best practice
# but is included for educational purposes.
# Create an array of dog names (not using the dictionary)
dogz = ['Rocky', 'Bella', 'Daisy']
dog_activities = [None, None, None]

for i, dog in enumerate(dogz):
    if dog == 'Rocky':
        dog_activities[i] = 'Chasing'
    
