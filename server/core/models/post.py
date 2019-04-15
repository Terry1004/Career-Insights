from flask import current_app
from .user import User
from .tag import Tag
from .comment import Comment
from ..utils import to_like_string


class Post:

    def __init__(self, uni, title, content, post_id=None, time_posted=None):
        self.uni = uni
        self.title = title
        self.content = content
        self.id = post_id
        self.time_posted = time_posted

    def __eq__(self, post):
        return self.id == post.id

    def __hash__(self):
        return hash(self.id)

    @classmethod
    def fetchall(cls, post_type, recent=None):
        sql_string = """
            WITH LastComments AS (
                SELECT postId, MAX(timePosted) AS timePosted
                FROM Comments
                GROUP BY postId
            )
            SELECT p.uni, p.title, p.content, p.id, p.timePosted
            FROM Posts p JOIN Tags t
            ON p.id = t.postId
            LEFT JOIN LastComments l
            ON p.id = l.postId
            WHERE t.postType = %s
            ORDER BY (
                CASE
                    WHEN l.timePosted is NULL THEN p.timePosted
                    ELSE l.timePosted
                END
            ) DESC
        """
        with current_app.database.begin() as connection:
            cursor = connection.execute(sql_string, post_type)
            if recent:
                posts_raw = cursor.fetchmany(recent)
            else:
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
            WHERE LOWER(title) LIKE %s ESCAPE ''
        """
        with current_app.database.begin() as connection:
            cursor = connection.execute(sql_string, to_like_string(title))
            posts_raw = cursor.fetchall()
            posts = [cls(*post_raw) for post_raw in posts_raw]
        return posts

    @classmethod
    def find_by_name(cls, name):
        sql_string = """
            SELECT p.uni, p.title, p.content, p.id, p.timePosted
            FROM Posts p JOIN Users u
            ON p.uni = u.uni
            WHERE LOWER(u.userName) LIKE %s ESCAPE ''
        """
        with current_app.database.begin() as connection:
            cursor = connection.execute(sql_string, to_like_string(name))
            posts_raw = cursor.fetchall()
            posts = [cls(*post_raw) for post_raw in posts_raw]
        return posts

    @classmethod
    def find_by_company(cls, company):
        sql_string = """
            SELECT p.uni, p.title, p.content, p.id, p.timePosted
            FROM Posts p JOIN Tags t
            ON p.id = t.postId
            WHERE LOWER(t.company) LIKE %s ESCAPE ''
        """
        with current_app.database.begin() as connection:
            cursor = connection.execute(sql_string, to_like_string(company))
            posts_raw = cursor.fetchall()
            posts = [cls(*post_raw) for post_raw in posts_raw]
        return posts

    @classmethod
    def find_by_content(cls, content):
        sql_string = """
            SELECT uni, title, content, id, timePosted
            FROM Posts p
            WHERE LOWER(content) LIKE %s ESCAPE ''
        """
        with current_app.database.begin() as connection:
            cursor = connection.execute(sql_string, to_like_string(content))
            posts_raw = cursor.fetchall()
            posts = [cls(*post_raw) for post_raw in posts_raw]
        return posts

    @classmethod
    def find_by_domain(cls, domain):
        sql_string = """
            SELECT p.uni, p.title, p.content, p.id, p.timePosted
            FROM Posts p JOIN Tags t
            ON p.id = t.postId
            WHERE LOWER(t.domain) LIKE %s ESCAPE ''
        """
        with current_app.database.begin() as connection:
            cursor = connection.execute(sql_string, to_like_string(domain))
            posts_raw = cursor.fetchall()
            posts = [cls(*post_raw) for post_raw in posts_raw]
        return posts

    @classmethod
    def find_by_hashtags(cls, hashtags):
        with_string = """
            WITH TagsExpanded AS (
                SELECT *
                FROM Tags, UNNEST(hashtags) hashtag
            )
        """
        single_sql_string = """
            SELECT DISTINCT ON (p.id)
            p.uni, p.title, p.content, p.id, p.timePosted
            FROM Posts p JOIN TagsExpanded t
            ON p.id = t.postId
            WHERE LOWER(t.hashtag) LIKE %s ESCAPE ''
            OR LOWER(t.domain) LIKE %s ESCAPE ''
        """
        sql_string = with_string + '\n' + '\nUNION\n'.join(
            single_sql_string for _ in hashtags
        )
        placeholders = []
        for hashtag in hashtags:
            for _ in range(2):
                placeholders.append(to_like_string(hashtag))
        with current_app.database.begin() as connection:
            cursor = connection.execute(sql_string, placeholders)
            posts_raw = cursor.fetchall()
            posts = [cls(*post_raw) for post_raw in posts_raw]
        return posts

    @classmethod
    def find_by_keywords(cls, keywords):
        with_string = """
            WITH TagsExpanded AS (
                SELECT *
                FROM Tags, UNNEST(hashtags) hashtag
            )
        """
        single_sql_string = """
            SELECT DISTINCT ON (p.id)
            p.uni, p.title, p.content, p.id, p.timePosted
            FROM Posts p JOIN TagsExpanded t
            ON p.id = t.postId
            JOIN Users u
            ON p.uni = u.uni
            WHERE LOWER(p.title) LIKE %s ESCAPE ''
            OR LOWER(p.content) LIKE %s ESCAPE ''
            OR LOWER(u.userName) LIKE %s ESCAPE ''
            OR LOWER(t.company) LIKE %s ESCAPE ''
            OR LOWER(t.position) LIKE %s ESCAPE ''
            OR LOWER(t.domain) LIKE %s ESCAPE ''
            OR LOWER(t.hashtag) LIKE %s ESCAPE ''
        """
        sql_string = with_string + '\n' + '\nUNION\n'.join(
            single_sql_string for _ in keywords
        )
        placeholders = []
        for keyword in keywords:
            for _ in range(7):
                placeholders.append(to_like_string(keyword))
        with current_app.database.begin() as connection:
            cursor = connection.execute(sql_string, placeholders)
            posts_raw = cursor.fetchall()
            posts = [cls(*post_raw) for post_raw in posts_raw]
        return posts

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

    @property
    def num_comments(self):
        if not self.id:
            return None
        else:
            sql_string = """
                SELECT COUNT(*)
                FROM Comments
                WHERE postId = %s
            """
            with current_app.database.begin() as connection:
                cursor = connection.execute(sql_string, self.id)
                count = cursor.fetchone()[0]
            return count

    @property
    def last_comment(self):
        if not self.id:
            return None
        else:
            sql_string = """
                SELECT postId, commentId, uni, content, timePosted
                FROM Comments
                WHERE postId = %s
                ORDER BY timePosted DESC
            """
            with current_app.database.begin() as connection:
                cursor = connection.execute(sql_string, self.id)
                comment_raw = cursor.fetchone()
            if comment_raw:
                return Comment(*comment_raw)
            else:
                return None

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
