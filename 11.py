def return_hello():
    return 'hello'

assert return_hello() != 'goodbye'
# checks if the statement is true

print("Change the == to != so that the assertion comes out True")

'''
File "/home/chett/031124/p3/01-python-debugging/11.py", line 4, in <module>
    assert return_hello() == 'goodbye'
AssertionError
'''