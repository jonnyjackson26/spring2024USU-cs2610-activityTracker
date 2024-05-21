from django.urls import path
from . import views

urlpatterns = [
    path('',view=views.index),
    path('new-activity/',view=views.newActivity),
    path('new-activity/createNewActivity/',view=views.createNewActivity),
    path('activity/<int:id>/',view=views.showActivity), 
    path('activity/<int:id>/createTimeLog/',view=views.createTimeLog),
    path('activity/<int:id>/createTimeLog/newTimeLog/',view=views.newTimeLog),
]