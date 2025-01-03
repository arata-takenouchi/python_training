# def print_more(func):
#     def wrapper(*args, **kwargs):
#         print('func:', func.__name__)
#         print('args:', args)
#         print('kwargs:', kwargs)
#         result = func(*args, **kwargs)
#         print('result:', result)
#         return result
#     return wrapper
#
# def print_info(func):
#     def wrapper(*args, **kwargs):
#         print('start')
#         result = func(*args, **kwargs)
#         print('end')
#         return result
#     return wrapper
#
# @print_info
# @print_more
# def add_num(a, b):
#     return (a + b)
#
# r = add_num(10, 20)
# print(r)

# @print_info
# def sub_num(a, b):
#     return a - b


# lambda
# l = ['Mon', 'tue', 'Wed', 'Thu', 'fri', 'sat', 'Sun']
#
# def change_words(words, func):
#     for word in words:
#         print(func(word))

# def sample_func(word):
#     return word.capitalize()

# def sample_func2(word):
#     return word.lower()

# sample_func = lambda word: word.capitalize()

# change_words(l, lambda word: word.capitalize())
# change_words(l, lambda word: word.lower())


# l = ['Good morning', 'Good afternoon', 'Good night']
def counter(num=10):
    for _ in range(num):
        yield 'run'

def greeting():
    yield 'Good morning'
    # for i in range(10):
    #     print(i)
    yield 'Good afternoon'
    # for i in range(10):
    #     print(i)
    yield 'Good night'

# for g in greeting():
#     print(g)

g = greeting()
c = counter()

print(next(g))

print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))

print(next(g))

print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))

print(next(g))
# print(next(g))