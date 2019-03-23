def get_db_url(config):
    url_format = config['DATABASE_URL_FORMAT']
    user = config['DATABASE_USER']
    password = config['DATABASE_PASSWORD']
    host = config['DATABASE_HOST']
    port = config['DATABASE_PORT']
    dbName = config['DATABASE_NAME']
    return url_format.format(user, password, host, port, dbName)
