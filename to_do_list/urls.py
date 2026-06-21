from django.urls import path
from . import views

urlpatterns = [
    path('', views.TaskListView.as_view(), name='task_list'),
    path('add/', views.TaskCreateView.as_view(), name='task_add'),
    path('toggle/<int:pk>/', views.TaskToggleView.as_view(), name='toggle_task'),
    path('delete/<int:pk>/', views.TaskDeleteView.as_view(), name='delete_task'),
]
