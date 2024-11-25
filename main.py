users: list = [
    {'name': 'Patryk', 'posts': 1, 'city': 'Warszawa'},
    {'name': 'Dominik', 'posts': 3, 'city': 'Łódź'},
    {'name': 'Szymon z wąsem', 'posts': 5, 'city': 'Kutno'},
    {'name': 'Szymon', 'posts': 7, 'city': 'Pabianice'},
    {'name': 'Patryk', 'posts': 9, 'city': 'Szczecin'},
    {'name': 'Aleksandra', 'posts': 1, 'city': 'Zamość'},
    {'name': 'Julia', 'posts': 1, 'city': 'Łuków'},
    {'name': 'Karolina', 'posts': 3, 'city': 'Kielce'},
    {'name': 'Amelia', 'posts': 5, 'city': 'Gniezno'},
    {'name': 'Szymon', 'posts': 7, 'city': 'Opole'},

]
#TODO please update user list

print(f'Witaj {users[0]['name']}!')
for user in users[1:]:
    print(f'twój znajomy {user['name']},z {user['city']}, opublikował {user['posts']} postów')
# for idx, _ in enumerate(users[1:]):
#     print(f'twój znajomy {users[idx]}, opublikował {postow[idx]} postów')
