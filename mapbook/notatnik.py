users: list = [
    {'name': 'Patryk', 'posts': 1, 'city': 'Warszawa'},
    {'name': 'Patryk', 'posts': 1, 'city': 'Warszawa'},
    {'name': 'Tomek', 'posts': 1, 'city': 'Warszawa'},
    {'name': 'Julia', 'posts': 1, 'city': 'Warszawa'},

]

def remove_user(userlist:list)->None:
    user_to_find:str=input("podaj imię do usunięcia:")
    for user in userlist:
        if user['name'] == user_to_find:
            print(f'usuwam: {user}')
            userlist.remove(user)

remove_user(users)

for user in users:
    print(user)
# print(new_user)