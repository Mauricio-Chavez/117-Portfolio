from django.urls import path

from .views import project_list
from .views import project_new

urlpatterns = [
    path('', project_list, name='project_list'),
    path('new/', project_new, name='project_new'),
]
