people = []

def create_new_person(name_param:str, age_param:int):
    new_person = { 'name': name_param, 'age': age_param }
    people.append(new_person)
    return new_person

def remove_person(person:dict):
    people.remove(person)

sakib = create_new_person('Sakib', 15)
chett = create_new_person('Chett', 101)

print( sakib )

remove_person(sakib)

print( people )

'''
File "/home/chett/031124/p3/01-python-debugging/09.py", line 9, in remove_person
    people.remove(person)
ValueError: list.remove(x): x not in list
'''