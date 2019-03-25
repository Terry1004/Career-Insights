from flask import current_app
from werkzeug.security import generate_password_hash, check_password_hash


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
    def findByUni(cls, uni):
        sqlString = """
            SELECT uni, password, email, personalDescription, username, major
            FROM Users
            WHERE uni = %s
        """
        with current_app.database.begin() as connection:
            cursor = connection.execute(sqlString, uni)
            user = cursor.fetchone()
        if not user:
            return None
        else:
            return cls(*user, hash=False)

    def save(self, update=False):
        insertString = """
            INSERT INTO Users (
                uni, password, email, personalDescription, username, major
            )
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        updateString = """
            UPDATE Users
            SET password = %s, email = %s,
            personalDescription = %s, username = %s, major = %s
            WHERE uni = %s
        """
        with current_app.database.begin() as connection:
            if not update:
                connection.execute(
                    insertString,
                    (
                        self.uni, self.password, self.email,
                        self.personal_des, self.username, self.major
                    )
                )
            else:
                connection.execute(
                    updateString,
                    (
                        self.password, self.email, self.personal_des,
                        self.username, self.major, self.uni
                    )
                )
