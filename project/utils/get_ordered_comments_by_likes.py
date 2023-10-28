from models.comment import Comment

def sort_key(e:Comment)->int:
    return e.like_count


def get_ordered_comments_by_likes(comments:list)->list:
    
    sorted_comments = sorted(comments, key=sort_key, reverse=True)
    return sorted_comments


