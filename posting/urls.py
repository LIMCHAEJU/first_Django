from django.urls import path

from posting import views

urlpatterns = [
    path('', views.getTaskList, name='getTaskList'),
    path('addTask', views.addTask, name='addTask')
]