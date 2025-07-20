def has_voted(user, voted_users):
    return user in voted_users

def mark_voted(user, voted_users):
    voted_users.add(user)
