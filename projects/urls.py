from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('getm',views.get_message),
    path('postm', views.post_message)
]