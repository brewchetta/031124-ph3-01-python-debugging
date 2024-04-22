my_string = 6

my_number = 5

def add(param1:int, param2:int):
    return param1 + param2

print( add(my_string, my_number) )

'''
File "/home/chett/031124/p3/01-python-debugging/02.py", line 6, in add
    return param1 + param2
TypeError: can only concatenate str (not "int") to str
'''