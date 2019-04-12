from collections import defaultdict
from flask import current_app
from .user import User


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
    def fetchall(cls, post_id):
        sql_string = """
            SELECT r.commentId,
            c.postId, c.commentId, c.uni, c.content, c.timePosted
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
        return comments

    @classmethod
    def find_by_id(cls, post_id, comment_id):
        sql_string = """
            SELECT postId, commentId, uni, content, timePosted
            FROM Comments
            WHERE postId = %s AND commentId = %s
        """
        with current_app.database.begin() as connection:
            cursor = connection.execute(sql_string, (post_id, comment_id))
            comment_raw = cursor.fetchone()
            comment = cls(*comment_raw)
        return comment

    @classmethod
    def get_max_id(cls, post_id):
        sql_string = """
            SELECT MAX(commentId)
            FROM Comments
            WHERE postId = %s
        """
        with current_app.database.begin() as connection:
            cursor = connection.execute(sql_string, post_id)
            max_id = cursor.fetchone()[0]
        if max_id is not None:
            return max_id
        else:
            return 1

    @property
    def user(self):
        sql_string = """
            SELECT uni, password, email, personalDescription, username, major
            FROM Users
            WHERE Users.uni = %s
        """
        with current_app.database.begin() as connection:
            cursor = connection.execute(sql_string, self.uni)
            user = cursor.fetchone()
        if not user:
            return None
        else:
            return User(*user, hash=False)

    def save(self, comment_id=None, update=False):
        insert_comment_string = """
            INSERT INTO Comments (
                postId, commentId, uni, content
            ) VALUES (%s, %s, %s, %s)
        """
        insert_reply_string = """
            INSERT INTO Replies (
                postId, commentId, replyId
            ) VALUES (%s, %s, %s)
        """
        update_comment_string = """
            UPDATE Comments
            SET content = %s
            WHERE postId = %s AND commentId = %s
        """
        with current_app.database.begin() as connection:
            if not update:
                connection.execute(
                    insert_comment_string,
                    (self.post_id, self.id, self.uni, self.content)
                )
                if comment_id is not None:
                    connection.execute(
                        insert_reply_string,
                        (self.post_id, comment_id, self.id)
                    )
            else:
                connection.execute(
                    update_comment_string,
                    (self.content, self.post_id, self.id)
                )

    def destroy(self):
        sql_string = """
            DELETE FROM Comments
            WHERE postId = %s AND commentId = %s
        """
        with current_app.database.begin() as connection:
            connection.execute(sql_string, (self.post_id, self.id))
