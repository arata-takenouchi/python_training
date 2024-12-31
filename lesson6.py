r = [1,2,3,4,5,1,2,3]
print(r.index(3, 3))

print(r.count(3))

if 100 in r:
    print('exist')

r.sort()
print(r)
r.sort(reverse=True)
print(r)
r.reverse()
print(r)

s = 'My name is Mike.'
to_split = s.split(' ')
print(to_split)

x = ' ### '.join(to_split)
print(x)

print('\n===============\n')

i = [1,2,3,4,5]
j = i
j[0] = 100
print(i)
print(j)

x = [1,2,3,4,5]
y = x.copy()
# y = x[:]
y[0] = 100
print(y)
print(x)

x = 20
y = x
y = 5
print(id(x), id(y))
x = ['a', 'b']
y = x
y[0] = 'p'
print(x, y)
print(id(x), id(y))