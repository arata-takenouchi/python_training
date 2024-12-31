num_tuple = (10,20)
print(num_tuple)

x, y = num_tuple
print(x,y)

i = 10
j = 20
tmp = i
i = j
j = tmp
print(i, j)

a = 100
b = 200
a, b = b, a
print(a, b)

print('\n-------------\n')

chose_from_two = ('A', 'B', 'C')
answer = []
answer.append('A')
answer.append('C')

print(chose_from_two)
print(answer)