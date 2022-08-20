from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('get_projects',views.get_projects),
    path('add_project', views.add_project),
    path('updated_project/<str:pk>', views.updated_project),
    path('updated_drag_project/<str:pk>',views.updated_drag_project)
]