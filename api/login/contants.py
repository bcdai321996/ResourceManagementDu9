from rest_framework import status


def get_response(code):
    response = {
        'code': 999,
        'message': 'System busy, please try again later !',
        'status_code': status.HTTP_200_OK,
    }

    if code is not None:
        response['code'] = code

    return response
