one = 1
two = 2

def compare_numbers(num_one:int, num_two:int):
    if num_one > num_two:
        return "Number one is greater"
    elif num_one < num_two:
        return "Number two is greater"
    else:
        return "The numbers are equal"

print( compare_numbers(one, two) )

'''
File "/home/chett/031124/p3/01-python-debugging/03.py", line 5, in compare_numbers
    if num_one > num_two:
TypeError: '>' not supported between instances of 'int' and 'str'
'''