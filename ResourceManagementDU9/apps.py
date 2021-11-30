
from django.apps import AppConfig
import sys


class AppGlobalConfig(AppConfig):
    name = 'ResourceManagementDU9'

    def ready(self):
        try:
            print('<<<<<-------------------------- StartUp --------------------------->>>>>')
            print('========================================================================')


            print('<<<<<--------------------------- Done ----------------------------->>>>>')
            print('========================================================================')

        except Exception as e:
            print('ResourceManagementDU9.apps.AppGlobalConfig -> ready -> ex: ', e)
            sys.exit(0)