from flask import current_app
from .user import User


class Post:

    def __init__(self, uni, title, content, post_id=None, time_posted=None):
        self.uni = uni
        self.title = title
        self.content = content
        self.id = post_id
        self.time_posted = time_posted

    @classmethod
    def fetchall(cls):
        sql_string = """
            SELECT uni, title, content, id, timePosted
            FROM Posts
        """
        with current_app.database.begin() as connection:
            cursor = connection.execute(sql_string)
            posts_raw = cursor.fetchall()
            posts = [cls(*post_raw) for post_raw in posts_raw]
        return posts

    @classmethod
    def find_by_id(cls, post_id):
        sql_string = """
            SELECT uni, title, content, id, timePosted
            FROM Posts
            WHERE id = %s
        """
        with current_app.database.begin() as connection:
            cursor = connection.execute(sql_string, post_id)
            post = cursor.fetchone()
        if not post:
            return None
        else:
            return cls(*post)

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

    def save(self, update=False):
        insert_string = """
            INSERT INTO Posts (
                uni, title, content
            ) VALUES (%s, %s, %s)
        """
        update_string = """
            UPDATE Posts
            SET title = %s, content = %s
            WHERE id = %s
        """
        with current_app.database.begin() as connection:
            if not update:
                connection.execute(
                    insert_string,
                    (self.uni, self.title, self.content)
                )
            else:
                connection.execute(
                    update_string,
                    (self.title, self.content, self.id)
                )
