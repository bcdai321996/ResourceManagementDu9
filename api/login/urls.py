from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login_requester),
    path('get_data/', views.btn_get_data),

]
