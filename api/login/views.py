from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.decorators import renderer_classes
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from . import contants
from . import models


@api_view(['POST'])
@parser_classes([JSONParser])
@renderer_classes([JSONRenderer])
def btn_get_data(request, format=None):
    response = contants.get_response(None)

    try:
        request_data = request.data

        # Validate obj_data_input
        # if validate.validate_sample(obj_data_input) == False:
        # response['code'] = 1
        # return Response(response)

        obj_data_output = models.btn_get_data()

        code_output = obj_data_output['code']
        data = obj_data_output['list_user']

        response = contants.get_response(code_output)
        response['data'] = data

    except Exception as e:
        print('login.views -> btn_get_data -> ex: ', e)

    return Response(response)


@api_view(['POST'])
@parser_classes([JSONParser])
@renderer_classes([JSONRenderer])
def get_by_id(request, format=None):
    response = contants.get_response(None)

    try:
        request_data = request.data

        # Validate obj_data_input
        # if validate.validate_sample(obj_data_input) == False:
        # response['code'] = 1
        # return Response(response)
        id_user = request_data['id']
        obj_data_output = models.get_by_id(id_user)

        code_output = obj_data_output['code']
        data = obj_data_output['user']

        response = contants.get_response(code_output)
        response['data'] = data

    except Exception as e:
        print('login.views -> btn_get_data -> ex: ', e)

    return Response(response)
