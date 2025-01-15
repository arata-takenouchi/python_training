import requests

r = requests.get('http://127.0.0.1:5000/employee/arata')
print(r.text)

r = requests.post('http://127.0.0.1:5000/employee', data={'name': 'arata'})
print(r.text)

r = requests.delete('http://127.0.0.1:5000/employee', data={'name': 'arata'})
print(r.text)

r = requests.put('http://127.0.0.1:5000/employee', data={
    'name': 'arata',
    'new_name': 'takenouchi'
})
print(r.text)