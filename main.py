users: list = [
    {'name': 'Patrycja', 'posts': 1, 'city': 'Warszawa'},
    {'name': 'Dominik', 'posts': 3, 'city': 'Warszawa'},
    {'name': 'Szymon z wąsem', 'posts': 5, 'city': 'Warszawa'},
    {'name': 'Szymon', 'posts': 7, 'city': 'Warszawa'},
    {'name': 'Patryk', 'posts': 9, 'city': 'Warszawa'},

]
#TODO please update user list

print(f'Witaj {users[0]['name']}!!')
for user in users[1:]:
    print(f'twój znajomy {user['name']},z {user['city']}, opublikował {user['posts']} postów')
# for idx, _ in enumerate(users[1:]):
#     print(f'twój znajomy {users[idx]}, opublikował {postow[idx]} postów')
