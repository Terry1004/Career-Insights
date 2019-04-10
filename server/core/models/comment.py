from collections import defaultdict
from flask import current_app


def traverse(tree, curr, res, depth):
    if curr:
        res.append((depth, curr))
        node_id = curr.id
    else:
        node_id = None
    children = sorted(
        tree.get(node_id, []),
        key=lambda reply: reply.time_posted
    )
    for child in children:
        traverse(tree, child, res, depth + 1)


class Comment:

    def __init__(
        self, post_id, comment_id, uni, content, time_posted=None
    ):
        self.post_id = post_id
        self.id = comment_id
        self.uni = uni
        self.content = content
        self.time_posted = time_posted

    @classmethod
    def find_all_comments(cls, post_id):
        sql_string = """
            SELECT r.commentId,
            c.postId, c.commentId, c.uni, c.timePosted, c.content
            FROM Comments c LEFT JOIN Replies r
            ON c.postId = r.postId AND c.commentId = r.replyId
            WHERE c.postId = %s
        """
        comment_tree = defaultdict(list)
        comment_tree[None] = []
        with current_app.database.begin() as connection:
            cursor = connection.execute(sql_string, post_id)
            for row in cursor:
                comment_id, *reply_raw = row
                reply = cls(*reply_raw)
                comment_tree[comment_id].append(reply)
        comments = []
        traverse(comment_tree, None, comments, -1)
        print(comment_tree)
        return comments
