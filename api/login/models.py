from ultils import mysql_connection
from ultils import response_json


def btn_get_data():
    connection = None
    cursor = None
    response = response_json.get_response(None)

    try:
        connection = mysql_connection.get_connection()
        cursor = connection.cursor()

        sql = "SELECT * FROM user "
        cursor.execute(sql)  # Execute sql query
        data = cursor.fetchall()  # Fetch data to array

        response['list_user'] = data
        response['code'] = 0

    except Exception as e:
        print('login.models -> btn_get_data -> ex: ', e)

    finally:
        if connection is not None:
            connection.close()

        if cursor is not None:
            cursor.close()

    return response


def get_by_id(id_user):
    connection = None
    cursor = None
    response = response_json.get_response(None)

    try:
        connection = mysql_connection.get_connection()
        cursor = connection.cursor()

        sql = "SELECT * FROM user WHERE id = %s "
        cursor.execute(sql, id_user)  # Execute sql query
        data = cursor.fetchone()  # Fetch data to array

        response['user'] = data
        response['code'] = 0

    except Exception as e:
        print('login.models -> btn_get_data -> ex: ', e)

    finally:
        if connection is not None:
            connection.close()

        if cursor is not None:
            cursor.close()

    return response
