def rate_sort(user):
    return user.rate

def select_top_users_by_rate(users, top_size):
    selected_users = sorted(users, key=rate_sort, reverse=True)

    return selected_users[:top_size]
