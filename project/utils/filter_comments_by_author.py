from models.user import User

def filter_comments_by_author(comments:list, author:User)->list:
    author_comments = []
    for comment in comments:
        if comment.author_id == author.id:
            author_comments.append(comment)
    
    
    return author_comments

