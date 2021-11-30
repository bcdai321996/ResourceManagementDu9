import ResourceManagementDU9.settings as settings
import pymysql.cursors


def get_connection():
    connection = None

    try:
        connection = pymysql.connect(
            host=settings.DB_HOST,
            port=int(settings.DB_PORT),
            db=settings.DB_NAME,
            user=settings.DB_USER,
            password=settings.DB_PASSWORD,
            charset=settings.DB_CHARSET,
            cursorclass=pymysql.cursors.DictCursor
        )

    except Exception as ex:
        print("mysql_connection -> get_connection -> exception: ", ex)

    return connection
