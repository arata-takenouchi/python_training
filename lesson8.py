x = {'a': 1}
y = x
y['a'] = 1000

print(x)
print(y)

x = {'a': 1}
y = x.copy()
y['a'] = 1000
print(x)
print(y)

print('\n----------------\n')

fruits = {
    'apple': 100,
    'banana': 200,
    'orange': 300,
}
print(fruits['apple'])