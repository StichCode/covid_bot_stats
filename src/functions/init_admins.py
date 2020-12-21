from config import CONFIG


def insert_admins(cache):
    users_id = cache.get('users', column='id')
    for user in CONFIG.admins:
        if not users_id:
            cache.put_user(user, True, True)
        for i in users_id:
            if user not in i:
                cache.put_user(user, True, True)
