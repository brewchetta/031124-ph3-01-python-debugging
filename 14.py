bundt_cake_ingredients = ['flour', 'baking powder', 'baking soda', 'butter', 'sugar', 'eggs', 'buttermilk', 'vanilla']

# 'flour, baking powder, baking soda, ....'

def make_cake(name:str, ingredients_list:list):

    return f"Making a {name} with these ingredients: { ', '.join(ingredients_list) }"


bundt_cake = make_cake( "BUNDT CAKE", bundt_cake_ingredients )

print( bundt_cake )

'''
File "/home/chett/031124/p3/01-python-debugging/14.py", line 5
    return f"Making a {name} with these ingredients: { ", ".join(ingredients_list) }"
           ^
SyntaxError: f-string: expecting '}'
'''