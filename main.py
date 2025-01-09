def base(x):
    def plus(y):
        return x + y
    return plus
plus = base(10)
print(plus(10))
print(plus(30))

i = 0
def add_num():
    def plus(y):
        return i + y
    return plus
i = 10
plus = add_num()
print(plus(10))
print(plus(30))
i = 100
print(plus(30))

# import os
# import sys
#
# import flask
#
# import roboter.contlorller.conversation
# # from roboter.czontlorller import conversation
#
# import settings

# class MainError(Exception):
#     pass
#
# def main():
#     try:
#         roboter.contlorller.conversation.talk_about_restaulant
#     except Exception as e:
#         print(e)
#     raise MainError('error')
#
# x = [(i, x) for i in [1,2,3,4] for x in [1,2,3]]
#
# d = {'key1': 'value1', 'key2', 'value2'}
# if 'key1' in d:
#     print('test')
#
# if 'key1' in d.keys():
#     print('test')
#
# for name, count in ranking.items():
#     print(name, count)
#
# if __name__ == 'main':
#     main()

# def t():
#     # num = []
#     for i in range(10):
#         yield i
#     #     num.append(i)
#     # return num
#
# for i in t():
#     print(i)

# def other_func(f):
#     print(f(10))
#
# def test_func(x):
#     return x * 2
#
# other_func(test_func)
# other_func(lambda x: x * 2)

# y = None
# y = 'gagagag'
# x = 1 if y else 2
# print(x)