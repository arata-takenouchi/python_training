from lesson_package.tools import utils

def sing():
    return 'sing######'

def cry():
    return utils.say_twice('cry######')

if __name__ == '__main__':
    print(sing())
    print('animal:', __name__)
