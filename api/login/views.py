from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.decorators import renderer_classes
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from ResourceManagementDU9 import jwt_authen
from . import contants
from . import models


# View request get all user
@api_view(['POST'])
@parser_classes([JSONParser])
@renderer_classes([JSONRenderer])
def btn_get_data(request, format=None):
    response = contants.get_response(None)

    try:
        obj_data_output = models.btn_get_data()

        code_output = obj_data_output['code']
        data = obj_data_output['list_user']

        response = contants.get_response(code_output)
        response['data'] = data

    except Exception as e:
        print('login.views -> btn_get_data -> ex: ', e)

    return Response(response)


# View request login
@api_view(['POST'])
@parser_classes([JSONParser])
@renderer_classes([JSONRenderer])
def login_requester(request):
    response = contants.get_response(None)
    try:
        data_input = request.data
        obj_login = {
            "user_name": data_input['user_name'],
            "password": data_input['password']
        }
        ip_request = request.META['REMOTE_ADDR']
        browser_request = request.META['HTTP_USER_AGENT']
        menu_access = ""
        token = ""
        data_output = models.login_requester(obj_login)
        code_output = data_output['code']
        if code_output == 0:
            user_id = data_output['user_id']
            token = jwt_authen.create_token(user_id, obj_login['user_name'], obj_login['password'], menu_access,
                                            ip_request, browser_request)
        response = contants.get_response(code_output)
        response['token'] = token
        response['code'] = code_output
    except Exception as e:
        print("login.views -> login_requester -> ex", e)

    return Response(response)


@api_view(['POST'])
@parser_classes([JSONParser])
@renderer_classes([JSONRenderer])
def logout_requester(request):
    print(request.META)
    response = contants.get_response_logout_requester(None)
    try:
        token = request.META['HTTP_AUTHORIZATION']
        check_token = jwt_authen.remove_token(token)
        if check_token:
            response = contants.get_response_logout_requester(0)
        else:
            response = contants.get_response_logout_requester(777)
    except Exception as e:
        print("authen.views -> logout -> ex", e)

    return Response(response)
