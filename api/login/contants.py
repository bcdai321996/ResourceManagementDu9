from rest_framework import status


def get_response(code):
    response = {
        'code': 999,
        'message': '',
        'status_code': status.HTTP_200_OK,
    }

    if code is not None:
        response['code'] = code

        if code == 0:
            response['message'] = 'Login Successfully'
        if code == 1:
            response['message'] = 'Password does not exist'

        if code == 2:
            response['message'] = 'User name does not exist '

    return response


def get_response_logout_requester(code):
    response = {
        'code': 200,
        'message': 'Execute successfully',
        'status_code': status.HTTP_200_OK
    }
    if code is not None:
        response['code'] = code
        if code == 0:
            response['message'] = 'Logout Successfully'
        if code == 777:
            response['message'] = 'Token does not exist'

    return response
