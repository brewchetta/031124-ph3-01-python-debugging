numbers_list = []

def average_numbers_in_list(num_list:list):
    if len( num_list ) == 0:
        return 0
    return sum(num_list) / len(num_list)

avg = average_numbers_in_list( numbers_list )

print( avg )

'''
File "/home/chett/031124/p3/01-python-debugging/15.py", line 4, in average_numbers_in_list
    return sum(num_list) / len(num_list)
ZeroDivisionError: division by zero
'''