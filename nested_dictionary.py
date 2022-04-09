users = {
    'einstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'bryan': {
        'first': 'bryan',
        'last': 'einstein',
        'location': 'Harvard',
    }
}

for username, user_info in users.items():
    print(f'\nUsername: {username}')
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
