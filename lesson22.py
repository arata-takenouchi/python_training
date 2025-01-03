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


l = [1,2,3]
i = 5
# del l

try:
    # () + l
    l[0]
    # l[i]
except IndexError as e:
    print(f'Index Error: {e}')
except NameError as e:
    print(f'Name Error: {e}')
except Exception as e:
    print(f'Other Error: {e}')
else:
    print('done')
finally:
    print('clean up')