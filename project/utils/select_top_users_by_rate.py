from models.user import User

def rate_sort(user:User):
    return user.rate

def select_top_users_by_rate(users:list, top_size:int)->list:
    selected_users = sorted(users, key=rate_sort, reverse=True)

    return selected_users[:top_size]
