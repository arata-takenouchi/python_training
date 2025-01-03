# def say_something():
#     s = 'hi'
#     return s
# result = say_something()
# print(result)
#
# def what_is_this(color):
#     if color == 'red':
#         return 'tomato'
#     elif color == 'green':
#         return 'green pepper'
#     else:
#         return "I don't know"
#
# result = what_is_this('green')
# result = what_is_this('red')
# result = what_is_this('yellow')
# print(result)


# num: int = 10
# def add_num(a: int, b: int) -> int:
#     return a + b
#
# r = add_num(10, 20)
# print(r)


# def menu(entree='beef', drink='wine', dessert='ice'):
#     print('entree=', entree)
#     print('drink=', drink)
#     print('dessert=', dessert)
#
# menu(entree='chicken')


# def test_func(x, l=None):
#     if l is None:
#         l = []
#     l.append(x)
#     return l

# y = [1,2,3]
# r = test_func(100, y)
# print(r)
#
# y = [1,2,3]
# r = test_func(200, y)
# print(r)

# r = test_func(100)
# print(r)
#
# r = test_func(100)
# print(r)


# def say_something(word, *args):
#     print(word)
#     for arg in args:
#         print(arg)
#
# say_something('hi', 'Mike', 'Nuncy')

# t = ('Mike', 'Nuncy')
# say_something('hi', *t)


def menu(food, *args, **kwargs):
    print(food)
    print(args)
    print(kwargs)
    # for k, v in kwargs.items():
    #     print(k, v)

menu('banana', 'apple', 'orange', entree='beef', drink='coffee')

# d = {
#     'entree': 'beef',
#     'drink': 'ice coffee',
#     'dessert': 'ice'
# }
# menu(**d)