from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('get_users',views.get_users),
    path('create_user',views.create_user),
]