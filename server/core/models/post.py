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

    @classmethod
    def find_by_keywords(cls, keywords):
        sql_string = """
            SELECT uni, title, content, id, timePosted
            FROM Posts
            WHERE LOWER(title) LIKE LOWER(%s)
            OR LOWER(content) LIKE LOWER(%s)
        """
        with current_app.database.begin() as connection:
            cursor = connection.execute(sql_string,str('%')+keywords+str('%'), str('%')+keywords+str('%'))
            posts_raw = cursor.fetchall()
            posts = [cls(*post_raw) for post_raw in posts_raw]
        return posts

    @classmethod
    def find_by_uni(cls, uni, title, keywords):
        sql_string = """
            SELECT uni, title, content, id, timePosted
            FROM Posts
            WHERE uni = %s 
        """
        with current_app.database.begin() as connection:
            cursor = connection.execute(sql_string,uni)
            posts_raw = cursor.fetchall()
            posts = [cls(*post_raw) for post_raw in posts_raw]
        return posts

    @classmethod
    def find_by_title(cls,title):
        sql_string = """
            SELECT uni, title, content, id, timePosted
            FROM Posts
            WHERE LOWER(title) LIKE LOWER(%s)
        """
        with current_app.database.begin() as connection:
            cursor = connection.execute(sql_string,str('%')+title+str('%'))
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
            WHERE LOWER(userName) LIKE LOWER(%s)
            )
            SELECT uni, title, content, id, timePosted
            FROM Posts
            WHERE uni
            IN (SELECT uni from temp)
        """
        with current_app.database.begin() as connection:
            cursor = connection.execute(sql_string, str('%')+name+str('%'))
            posts_raw = cursor.fetchall()
            posts = [cls(*post_raw) for post_raw in posts_raw]
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
            WHERE LOWER(company) LIKE LOWER(%s)
            )
            SELECT uni, title, content, id, timePosted
            FROM Posts
            WHERE id
            IN (SELECT postId from temp)
        """
        with current_app.database.begin() as connection:
            cursor = connection.execute(sql_string, str('%')+company+str('%'))
            posts_raw = cursor.fetchall()
            posts = [cls(*post_raw) for post_raw in posts_raw]
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
            WHERE id
            IN (SELECT postId from temp)
        """
        with current_app.database.begin() as connection:
            cursor = connection.execute(sql_string, str('%')+keywords+str('%'), str('%')+keywords+str('%'))
            posts_raw = cursor.fetchall()
            posts = [cls(*post_raw) for post_raw in posts_raw]
        if not posts:
            return None
        else:
            return posts
