dogs_list = ['Clifford', 'Scooby Doo', 'Balto']

def print_list_items(list_param:list):
    i = 0
    while i < len( dogs_list ):
        print(i)
        print(dogs_list[i])
        i += 1


print_list_items( dogs_list )

'''
File "/home/chett/031124/p3/01-python-debugging/13.py", line 6, in print_list_items
    print(dogs_list[i])
IndexError: list index out of range
'''