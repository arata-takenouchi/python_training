# """
# Test #########
# """
# animal = 'cat'

# def f():
#     """Test func doc"""
#     print(f.__name__)
#     print(f.__doc__)
    # global animal
    # animal = 'dog'
    # print('local', locals())
# f()
# print('global:', globals())
# print(__name__)


# l = [1,2,3]
# i = 5
# del l

# try:
    # () + l
    # l[0]
    # l[i]
# except IndexError as e:
#     print(f'Index Error: {e}')
# except NameError as e:
#     print(f'Name Error: {e}')
# except Exception as e:
#     print(f'Other Error: {e}')
# else:
#     print('done')
# finally:
#     print('clean up')


# raise IndexError('test error')
class UppercaseError(Exception):
    pass

def check():
    words = ['APPLE', 'orange', 'banana']
    for word in words:
        if word.isupper():
            raise UppercaseError(word)
try:
    check()
except UppercaseError as e:
    print('This is my fault. Go next')