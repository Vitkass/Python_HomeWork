import uuid


class User:
    def __init__(self, name):
        self.id = uuid.uuid4()
        self.name = name
        self.comments_count = 0
        self.rate = 0
        self.is_banned = False

    def edit_name(self, new_name):
        self.name = new_name

    def increment_rate(self):
        self.rate += 1

    def ban_user(self):
        self.is_banned = True

    def unban_user(self):
        if self.is_banned:
            self.is_banned = False

    def __repr__(self):

        banned = 'Not banned' if not self.is_banned else 'Is banned'
        user_info = f'''User Info: 
            Name: {self.name}, 
            Number of comments: {self.comments_count},
            Status: {banned},
            Rating: {self.rate} 
            '''
        
        return user_info
        
