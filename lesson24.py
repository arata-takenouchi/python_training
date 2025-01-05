class Person(object):
    def __init__(self, name):
        self.name = name
        print(self.name)

    def say_something(self):
        print(f'I am {self.name} hello')
        self.run(10)

    def run(self, num):
        print('run' * num)

    def __del__(self):
        print('good bye')

person = Person('Mike')
person.say_something()

del person

print('####')
