# File: ProjectChatBot.middleware.py
# Description: Migration token after Login
# Author             Date                       Change Description
# Bcdai            9/7/2020                     Create new function
from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin

from ResourceManagementDU9 import settings, jwt_authen
from ultils import global_config


# function middleware kiểm tra user sau khi login
class PermissionMiddleware(MiddlewareMixin):

    def process_request(self, request):
        try:
            url_request = request.META['PATH_INFO']
            ip_request = request.META['REMOTE_ADDR']
            server_name = request.META['SERVER_NAME']
            global_config.GLB_USER_IP_ADDRESS = ip_request
            global_config.GLB_USER_PC_NAME = server_name

            url_access_request = settings.API_URL_ACCESS
            url_access_request_flag = False

            for val1 in url_access_request:
                if url_request == val1:
                    url_access_request_flag = True
                    break

            if not url_access_request_flag:
                token_request = request.META['HTTP_AUTHORIZATION']
                flag_check_token = jwt_authen.vertify_token(token_request)
                print(flag_check_token)
                if flag_check_token:
                    permission_access_request = settings.API_PERMISSION_ACCESS
                    permission_access_request_flag = False

                    for val2 in permission_access_request:
                        if url_request.find(val2) != -1:
                            permission_access_request_flag = True
                            print("permission_access_request_flag", permission_access_request_flag)
                            break

                    if not permission_access_request_flag:
                        flag_check_permission = True

                else:
                    return JsonResponse(
                        {
                            "code": 333,
                            "message": "Token is incorrect"
                        }
                    )

        except Exception as e:
            print("PermissionMiddleware.process_request -> ex", e)
            return JsonResponse(
                {
                    "code": 333,
                    "message": "Token is incorrect"
                }
            )

    def process_response(self, request, response):
        if response.status_code != 200:
            return JsonResponse(
                {
                    "code": response.status_code,
                    "message": "ERROR"
                }
            )

        return response
