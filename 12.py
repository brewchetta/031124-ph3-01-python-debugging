from faker import Faker
from random import choice

fake = Faker()

def create_angry_bird():

    bird_dict = {
        'name': fake.name(),
        'anger_level': choice( range(5,11) )
    }

    return bird_dict


print( create_angry_bird() )

'''
File "/home/chett/031124/p3/01-python-debugging/12.py", line 1, in <module>
    from flaker import Faker
ModuleNotFoundError: No module named 'flaker'
'''