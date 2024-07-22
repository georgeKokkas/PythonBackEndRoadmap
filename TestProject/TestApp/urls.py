from django.urls import path
from .views import task_list, task_detail, TaskCreateView

urlpatterns = [
    path('', task_list, name='task_list'),
    path('<int:task_id>/', task_detail, name='task_detail'),
    path('create/', TaskCreateView.as_view(), name='task_create'),
]