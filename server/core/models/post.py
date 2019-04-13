from flask import current_app
from .user import User
from .tag import Tag


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
            ORDER BY timePosted DESC
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

    @classmethod
    def find_by_title(cls, title):
        sql_string = """
            SELECT uni, title, content, id, timePosted
            FROM Posts
            WHERE LOWER(title) LIKE %s
        """
        title = title.lower().replace('_', r'\_').replace('%', r'\%')
        with current_app.database.begin() as connection:
            cursor = connection.execute(sql_string, '%{}%'.format(title))
            posts_raw = cursor.fetchall()
            posts = [cls(*post_raw) for post_raw in posts_raw]
        return posts

    @classmethod
    def find_by_name(cls, name):
        sql_string = """
            SELECT p.uni, p.title, p.content, p.id, p.timePosted
            FROM Posts p JOIN Users u
            ON p.uni = u.uni
            WHERE LOWER(u.userName) LIKE %s
        """
        name = name.lower().replace('_', r'\_').replace('%', r'\%')
        with current_app.database.begin() as connection:
            cursor = connection.execute(sql_string, '%{}%'.format(name))
            posts_raw = cursor.fetchall()
            posts = [cls(*post_raw) for post_raw in posts_raw]
        return posts

    @classmethod
    def find_by_company(cls, company):
        sql_string = """
            SELECT p.uni, p.title, p.content, p.id, p.timePosted
            FROM Posts p JOIN Tags t
            ON p.id = t.postId
            WHERE LOWER(t.company) LIKE %s
        """
        company = company.lower().replace('_', r'\_').replace('%', r'\%')
        with current_app.database.begin() as connection:
            cursor = connection.execute(sql_string, '%{}%'.format(company))
            posts_raw = cursor.fetchall()
            posts = [cls(*post_raw) for post_raw in posts_raw]
        return posts

    # @classmethod
    # def find_by_keywords(cls, keywords):
    #     sql_string = """
    #         WITH temp AS
    #         (
    #         SELECT postId
    #         FROM Tags
    #         WHERE %s LIKE ANY (hashtags)
    #         OR domain LIKE %s
    #         )
    #         SELECT uni, title, content, id, timePosted
    #         FROM Posts
    #         WHERE id
    #         IN (SELECT postId from temp)
    #     """
    #     with current_app.database.begin() as connection:
    #         cursor = connection.execute(sql_string, keywords, str('%')+keywords+str('%'))
    #         posts_raw = cursor.fetchall()
    #         posts = [cls(*post_raw) for post_raw in posts_raw]
    #     if not posts:
    #         return None
    #     else:
    #         return posts

    @classmethod
    def get_max_id(cls):
        sql_string = """
            SELECT MAX(id)
            FROM Posts
        """
        with current_app.database.begin() as connection:
            cursor = connection.execute(sql_string)
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

    @property
    def tag(self):
        if not self.id:
            return None
        else:
            return Tag.find_by_post_id(self.id)

    def save(self, update=False):
        insert_string = """
            INSERT INTO Posts (
                uni, title, content
            ) VALUES (%s, %s, %s)
        """
        insert_string_id = """
            INSERT INTO Posts (
                id, uni, title, content
            ) VALUES (%s, %s, %s, %s)
        """
        update_string = """
            UPDATE Posts
            SET title = %s, content = %s
            WHERE id = %s
        """
        with current_app.database.begin() as connection:
            if not update:
                if not self.id:
                    connection.execute(
                        insert_string,
                        (self.uni, self.title, self.content)
                    )
                else:
                    connection.execute(
                        insert_string_id,
                        (self.id, self.uni, self.title, self.content)
                    )
            else:
                connection.execute(
                    update_string,
                    (self.title, self.content, self.id)
                )

    def destroy(self):
        delete_tag_string = """
            DELETE FROM Tags
            WHERE postId = %s
        """
        delete_post_string = """
            DELETE FROM Posts
            WHERE id = %s
        """
        with current_app.database.begin() as connection:
            connection.execute(delete_tag_string, self.id)
            connection.execute(delete_post_string, self.id)
