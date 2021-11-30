from datetime import datetime

import jwt

from ResourceManagementDU9 import settings

from ultils import global_config

jwt_token_memory_authenticator = []


def create_token(userid, username, password, menu_access, ip_request, browser_request):
    time_now_str = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    payload = {
        'userid': userid,
        'username': username,
        'password': password,
        'time': time_now_str,
        'ip': ip_request,
        'browser': browser_request,
        'menu_access': menu_access
    }
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256').decode("utf-8")
    for object_old in reversed(jwt_token_memory_authenticator):
        if object_old['user_name'] == username:
            time_old_str = object_old['time']
            time_old_fr = datetime.strftime(time_old_str, "%d-%m-%Y %H:%M:%S")
            time_now_fr = datetime.strftime(time_now_str, "%d-%m-%Y %H:%M:%S")
            time_diff = time_now_fr - time_old_fr
            time_diff_sec = time_diff.seconds / 60
            if time_diff_sec > 30:
                jwt_token_memory_authenticator.remove(object_old)

    user_memory_jwt = {
        'userid': userid,
        'username': username,
        'password': password,
        'token': token,
        'time': time_now_str,
        'ip': ip_request,
        'browser': browser_request,
        'menu_access': menu_access
    }

    jwt_token_memory_authenticator.append(user_memory_jwt)

    return token


def vertify_token(token):
    flag_check_token = False
    try:
        decode_token = jwt.decode(token, settings.SECRET_KEY, algorithms='HS256')
        userid = decode_token['userid']
        user_name = decode_token['username']
        password = decode_token['password']
        ip = decode_token['ip']
        browser = decode_token['browser']
        for object_old in reversed(jwt_token_memory_authenticator):
            if object_old["userid"] == userid and \
                object_old["username"] == user_name \
                and object_old["password"] == password \
                and object_old["ip"] == ip and object_old["browser"] == browser:
                time_old_str = object_old['time']
                time_now_str = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
                old_time_fr = datetime.strptime(time_old_str, '%d-%m-%Y %H:%M:%S')
                now_time_fr = datetime.strptime(time_now_str, '%d-%m-%Y %H:%M:%S')

                duration_time = now_time_fr - old_time_fr

                duration_minutes = duration_time.seconds / 60
                if duration_minutes > 30:
                    jwt_token_memory_authenticator.remove(object_old)
                    flag_check_token = False

                else:
                    object_old['time'] = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                    global_config.GLB_USER_ID = userid
                    global_config.GLB_USER_NAME = user_name

                    flag_check_token = True

                break
    except Exception as e:
        print('Token incorrect', e)

    return flag_check_token


def remove_token(token):
    flag_remove_token = False
    try:
        for object_old in reversed(jwt_token_memory_authenticator):
            if object_old['token'] == token:
                jwt_token_memory_authenticator.remove(token)
                flag_remove_token = True
                break
    except Exception as e:
        print('Token remove', e)
    return flag_remove_token
