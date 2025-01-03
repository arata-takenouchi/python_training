"""
Test #########
"""
animal = 'cat'

def f():
    """Test func doc"""
    print(f.__name__)
    print(f.__doc__)
    # global animal
    # animal = 'dog'
    # print('local', locals())
f()
# print('global:', globals())
print(__name__)