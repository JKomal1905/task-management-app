from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home_view, name='home'),
    path('add_task/', views.add_task_view, name='add_task'),
    path('task_done/<int:id>/', views.task_done_view, name='task_done'),
    path('task_undo/<int:id>/', views.task_undo_view, name='task_undo'),
    path('task_delete/<int:id>/', views.task_delete_view, name='task_delete'),
    path('delete_all/', views.delete_all_view, name='delete_all'),
    path('clear_all/', views.clear_all_view, name='clear_all'),
    path('remove_all/', views.remove_all_view, name='remove_all'),
    path('update_task/<int:id>/', views.update_task_view, name='update_task_view'),
]
