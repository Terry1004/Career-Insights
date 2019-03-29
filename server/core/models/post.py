from flask import current_app


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
            SELECT uni, title, content, id, timeposted
            FROM posts
        """
        with current_app.database.begin() as connection:
            cursor = connection.execute(sql_string)
            posts_raw = cursor.fetchall()
            posts = [cls(*post_raw) for post_raw in posts_raw]
        return posts
