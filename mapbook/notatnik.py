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

# remove_user(users)

def update_user(userlist:list)->None:
    user_to_find: str = input("podaj imię użytkownika do aktualizacji:")
    for user in userlist:
        if user['name'] == user_to_find:
            new_name: str = input("proszę podać nowe imię znajomego ")
            new_posts: int = int(input("podaj nową liczbę postów "))
            new_city: str = input("podaj nowe miasto ")
            user["name"] = new_name
            user["posts"] = new_posts
            user["city"] = new_city


update_user(users)


user_to_find:str=input("podaj imię użytkownika do aktualizacji:")
for user in users:
    if user['name'] == user_to_find:
        new_name: str = input("proszę podać nowe imię znajomego ")
        new_posts: int = int(input("podaj nową liczbę postów "))
        new_city: str = input("podaj nowe miasto ")
        user["name"]= new_name
        user["posts"]= new_posts
        user["city"] = new_city





for user in users:
    print(user)
# print(new_user)