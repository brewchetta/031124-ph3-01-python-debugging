def recursive_print_function(number:int):

    if number > 100:
        return "don't call yourself"

    print(number)
    recursive_print_function(number + 1)


recursive_print_function(1)

'''
File "/home/chett/031124/p3/01-python-debugging/16.py", line 5, in <module>
    recursive_print_function(1)
  File "/home/chett/031124/p3/01-python-debugging/16.py", line 3, in recursive_print_function
    recursive_print_function(number + 1)
  File "/home/chett/031124/p3/01-python-debugging/16.py", line 3, in recursive_print_function
    recursive_print_function(number + 1)
  File "/home/chett/031124/p3/01-python-debugging/16.py", line 3, in recursive_print_function
    recursive_print_function(number + 1)
  [Previous line repeated 992 more times]
  File "/home/chett/031124/p3/01-python-debugging/16.py", line 2, in recursive_print_function
    print(number)
RecursionError: maximum recursion depth exceeded while calling a Python object
'''