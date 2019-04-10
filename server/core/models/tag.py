from flask import current_app


class Tag:

    def __init__(
        self, post_id, post_type, rate,
        position, company, hashtags, domain, tag_id=None
    ):
        self.post_id = post_id
        self.post_type = post_type
        self.rate = rate
        self.position = position
        self.company = company
        self.hashtags = hashtags
        self.domain = domain
        self.id = tag_id

    @classmethod
    def find_by_post_id(cls, post_id):
        sql_string = """
            SELECT postId, postType, rate, position,
            company, hashtags, domain, id
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

    @property
    def hashtags_str(self):
        return '{{{}}}'.format(
            ','.join('"{}"'.format(hashtag) for hashtag in self.hashtags)
        )

    def save(self, update=False):
        insert_string = """
            INSERT INTO Tags (
                postId, postType, rate, position, company, hashtags, domain
            ) VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        update_string = """
            UPDATE Tags
            SET postType = %s, rate = %s, position = %s,
            company = %s, hashtags = %s, domain = %s
            WHERE id = %s
        """
        with current_app.database.begin() as connection:
            if not update:
                connection.execute(
                    insert_string,
                    (
                        self.post_id, self.post_type, self.rate, self.position,
                        self.company, self.hashtags_str, self.domain
                    )
                )
            else:
                connection.execute(
                    update_string,
                    (
                        self.post_type, self.rate, self.position,
                        self.company, self.hashtags_str, self.domain, self.id
                    )
                )
