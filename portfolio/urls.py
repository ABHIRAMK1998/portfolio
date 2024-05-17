from django.urls import path
from . import views

urlpatterns = [
    path('view/', views.view_portfolio, name='view_portfolio'),
    path('create/', views.create_portfolio, name='create_portfolio'),
    path('edit/', views.edit_portfolio, name='edit_portfolio'),
    path('view_project/', views.view_project, name='view_project'),
    path('create_project/', views.create_project, name='create_project'),
    path('edit_project', views.edit_project, name='edit_project'),
    path('project_home/',views.ProjectHome,name='project_home')
]
