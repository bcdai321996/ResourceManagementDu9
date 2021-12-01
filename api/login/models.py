from ultils import mysql_connection
from ultils import response_json


# Get all user
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


# Execute sql query login check username password
def login_requester(obj_login):
    connection = None
    cursor = None
    response = response_json.get_response(None)
    try:
        connection = mysql_connection.get_connection()
        cursor = connection.cursor()

        sql_select = "SELECT * FROM user WHERE LCASE(UserName) = LCASE(%s)"
        cursor.execute(sql_select, obj_login['user_name'])  # Execute sql query
        if cursor.rowcount > 0:
            for user in cursor.fetchall():
                if user['Password'] == obj_login['password']:
                    response['code'] = 0
                    response['user_id'] = user['Id']
                else:
                    response['code'] = 1
        else:
            response['code'] = 2

    except Exception as e:
        print('login.models -> login_requester -> ex: ', e)

    finally:
        if connection is not None:
            connection.close()

        if cursor is not None:
            cursor.close()

    return response
