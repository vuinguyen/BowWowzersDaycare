# BowWowzers Doggie Daycare Management System

from doggy_daycare import Dog, Daycare

# Initialize the daycare
bowwowzers = Daycare()
# Add a few dogs to the daycare
Rocky = Dog('Rocky', 'Schnoodle', '2020-01-01', 14)
Bella = Dog('Bella', 'Golden Retriever', '2019-05-15', 65)
Charlie = Dog('Charlie', 'Beagle', '2018-11-20', 30)
bowwowzers.add_dog(Rocky)
bowwowzers.add_dog(Bella)
bowwowzers.add_dog(Charlie)

# View all dogs in the daycare
bowwowzers.view_dogs()

# Check in a dog
bowwowzers.check_in('Rocky')

# Check in another dog
bowwowzers.check_in('Bella')

# View checked-in dogs
bowwowzers.view_checked_in_dogs()

# Modify the details of a dog
Rocky.favorite_activity = 'Chasing'

# Check out a dog
bowwowzers.check_out('Rocky')

# Check out another dog
bowwowzers.check_out('Bella')

# View checked-in dogs after check out
bowwowzers.view_checked_in_dogs()

# Remove a dog from the daycare
bowwowzers.remove_dog('Charlie')

# View all dogs in the daycare
bowwowzers.view_dogs()

