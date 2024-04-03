import requests

response = requests.get("https://randomuser.me/api/")





gender = response.json()['results'][0]['gender']


fisrt_name = response.json()['results'][0]['name']['first']

last_name = response.json()['results'][0]['name']['last']


title = response.json()['results'][0]['name']['title']
print(f'{title}. {fisrt_name} {last_name}')

age = response.json()['results'][0]['dob']['age']

print(f'Age: {age}')

cell = response.json()['results'][0]['cell']
phone = response.json()['results'][0]['phone']
print(f'Phone No :{phone}')
print(f'Cell No :{cell}')

