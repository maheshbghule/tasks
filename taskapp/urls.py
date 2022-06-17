from django.urls import path
from django import views
from .import views
urlpatterns = [
    path('', views.api_view, name="apioverview"),
    path('show', views.ShowAll, name='student-list'),
    path('view/<name>', views.ViewtaskName, name='view'),
    path('update/<name>', views.Updatetask, name='update'),
    path('add', views.Addtask, name='add'), 

]  