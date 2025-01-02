def say_something():
    # print('hi')
    s = 'hi'
    return s
# say_something()
result = say_something()
print(result)

def what_is_this(color):
    if color == 'red':
        return 'tomato'
    elif color == 'green':
        return 'green pepper'
    else:
        return "I don't know"

result = what_is_this('green')
result = what_is_this('red')
result = what_is_this('yellow')
print(result)