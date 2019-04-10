from flask import current_app


class Tag:

    def __init__(
        self, tag_id, post_id, post_type, rate,
        position, company, hashtags, domain
    ):
        self.id = tag_id
        self.post_type = post_type
        self.rate = rate
        self.position = position
        self.company = company
        self.hashtags = hashtags
        self.domain = domain

    @classmethod
    def find_by_post_id(cls, post_id):
        sql_string = """
            SELECT id, postId, postType, rate,
            position, company, hashtags, domain
            FROM Tags
            WHERE postId = %s
        """
        with current_app.database.begin() as connection:
            cursor = connection.execute(sql_string, post_id)
            tag = cursor.fetchone()
        if not tag:
            return None
        else:
            return cls(*tag)
