from django.urls import path
from . import views


urlpatterns = [
    path('get_data/', views.btn_get_data),
    path('login/', views.login_requester)
]
