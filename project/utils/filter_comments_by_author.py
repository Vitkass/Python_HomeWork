def filter_comments_by_author(comments, author):
    author_comments = []
    for comment in comments:
        if comment.author_id == author.id:
            author_comments.append(comment)
    
    
    return author_comments

