from flask import current_app


class Search:

    def __init__(self, uni, title, content, post_id=None, time_posted=None):
        self.uni = uni
        self.title = title
        self.content = content
        self.id = post_id
        self.time_posted = time_posted

    @classmethod
    def find_from_posts(cls, uni, title, keywords):
        sql_string = """
            SELECT uni, title, content, id, timePosted
            FROM Posts
            WHERE uni = %s 
            OR title LIKE %s 
            OR title LIKE %s
            OR content LIKE %s 
        """
        with current_app.database.begin() as connection:
            cursor = connection.execute(sql_string,uni,title, keywords, keywords)
            posts_raw = cursor.fetchall()
            posts = [cls(*post_raw) for post_raw in posts_raw]
        return posts

    @classmethod
    def find_by_name(cls, name):
        sql_string = """
            WITH temp AS 
            (
            SELECT uni 
            FROM Users
            WHERE userName LIKE %s
            )
            SELECT uni, title, content, id, timePosted
            FROM Posts
            WHERE uni = temp.uni
        """
        with current_app.database.begin() as connection:
            cursor = connection.execute(sql_string, name)
            posts = cursor.fetchall()
        if not posts:
            return None
        else:
            return posts

    @classmethod
    def find_by_company(cls, company):
        sql_string = """
            WITH temp AS 
            (
            SELECT postId 
            FROM Tags
            WHERE company LIKE %s
            )
            SELECT uni, title, content, id, timePosted
            FROM Posts
            WHERE id = temp.postId
        """
        with current_app.database.begin() as connection:
            cursor = connection.execute(sql_string, company)
            posts = cursor.fetchall()
        if not posts:
            return None
        else:
            return posts

    @classmethod
    def find_by_keywords(cls, keywords):
        sql_string = """
            WITH temp AS 
            (
            SELECT postId 
            FROM Tags
            WHERE hashtags LIKE %s
            OR domain LIKE %s
            )
            SELECT uni, title, content, id, timePosted
            FROM Posts
            WHERE id = temp.postId
        """
        with current_app.database.begin() as connection:
            cursor = connection.execute(sql_string, keywords, keywords)
            posts = cursor.fetchall()
        if not posts:
            return None
        else:
            return posts