def sort_key(e):
    return e.like_count


def get_ordered_comments_by_likes(comments):
    
    sorted_comments = sorted(comments, key=sort_key, reverse=True)
    return sorted_comments


