number_variable = 20

def add_to_number_variable(num:int):
    global number_variable
    number_variable += num
    return number_variable

print( add_to_number_variable(5) )

print( number_variable )

'''
File "/home/chett/031124/p3/01-python-debugging/05.py", line 4, in add_to_number_variable
    number_variable += num
UnboundLocalError: local variable 'number_variable' referenced before assignment
'''