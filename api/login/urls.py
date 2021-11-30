from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.btn_get_data),
    path('get_by_id/', views.get_by_id)
]
