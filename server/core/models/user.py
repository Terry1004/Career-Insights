from flask import current_app
from werkzeug.security import generate_password_hash


class User:

    def __init__(
        self, uni, password, email,
        personal_des='', username='', major='', hash=True
    ):
        self.uni = uni
        if hash:
            self.password = generate_password_hash(password)
        else:
            self.password = password
        self.email = email
        self.personal_des = personal_des
        self.username = username
        self.major = major

    @classmethod
    def find_by_uni(cls, uni):
        sql_string = """
            SELECT uni, password, email, personalDescription, username, major
            FROM Users
            WHERE uni = %s
        """
        with current_app.database.begin() as connection:
            cursor = connection.execute(sql_string, uni)
            user = cursor.fetchone()
        if not user:
            return None
        else:
            return cls(*user, hash=False)

    @classmethod
    def find_by_email(cls, email):
        sql_string = """
            SELECT uni, password, email, personalDescription, username, major
            FROM users
            WHERE email = %s
        """
        with current_app.database.begin() as connection:
            cursor = connection.execute(sql_string, email)
            user = cursor.fetchone()
        if not user:
            return None
        else:
            return cls(*user, hash=False)

    @property
    def num_posts(self):
        sql_string = """
            SELECT COUNT(*)
            FROM Posts
            WHERE uni = %s
        """
        with current_app.database.begin() as connection:
            cursor = connection.execute(sql_string, self.uni)
            count = cursor.fetchone()[0]
        return count

    @property
    def num_comments(self):
        sql_string = """
            SELECT COUNT(*)
            FROM Comments
            WHERE uni = %s
        """
        with current_app.database.begin() as connection:
            cursor = connection.execute(sql_string, self.uni)
            count = cursor.fetchone()[0]
        return count

    def save(self, update=False):
        insert_string = """
            INSERT INTO Users (
                uni, password, email, personalDescription, username, major
            )
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        update_string = """
            UPDATE Users
            SET password = %s, email = %s,
            personalDescription = %s, username = %s, major = %s
            WHERE uni = %s
        """
        with current_app.database.begin() as connection:
            if not update:
                connection.execute(
                    insert_string,
                    (
                        self.uni, self.password, self.email,
                        self.personal_des, self.username, self.major
                    )
                )
            else:
                connection.execute(
                    update_string,
                    (
                        self.password, self.email, self.personal_des,
                        self.username, self.major, self.uni
                    )
                )
