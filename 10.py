from faker import Faker

fake = Faker()

person = {
    'name': fake.name(),
    'address': fake.address(),
    'email': fake.email(),
    'phone': '999-999-9999'
}

print( person )

'''
File "/home/chett/031124/p3/01-python-debugging/10.py", line 9, in <module>
    'phone': fake.phone()
File "/home/chett/.pyenv/versions/3.8.13/lib/python3.8/site-packages/faker/proxy.py", line 130, in __getattr__
    return getattr(self._factories[0], attr)
AttributeError: 'Generator' object has no attribute 'phone'
'''