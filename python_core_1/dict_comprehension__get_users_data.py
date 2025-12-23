def get_users_data(users: list) -> dict:
    return {user[0]:
                {"username": user[1],
                 "email": user[2],
                 "password": user[3]}
            for user in users
            }
users = [
            (12, 'Maxim', 'maxim@example.com', 'UBg11eub42hge'),
            (13, 'Dmitro', 'dmitro@example.com', 'sdTioT36723fw'),
            (14, 'Roman', 'roman@example.com', 'hbFEkj34NggE2'),
            (15, 'Ivan', 'ivan@example.com', 'sdTioT36723fw'),
        ] # Four users
print(get_users_data(users))

"""
get_users_data(users) == {
    12: {
          'username': 'Maxim',
          'email': 'maxim@example.com',
          'password': 'UBg11eub42hge'
        },
}  # Result: dictionary with only one user id key
"""