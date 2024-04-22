cats_list = ["Octavia", "Ursula"]

def name_cats():
    cats_intros = []
    for cat in cats_list:
        cats_intros.append(f"Meow my name is {cat}")
    return cats_intros

print( name_cats() )

'''
File "/home/chett/031124/p3/01-python-debugging/06.py", line 4, in cats
    for cats in cats:
UnboundLocalError: local variable 'cats' referenced before assignment
'''