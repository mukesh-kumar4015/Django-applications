from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('home/', views.home),
    path('login/', views.user_login),
    path('register/', views.user_register),
    path('logout/', views.user_logout),
    path('forget_password/', views.forget_password),
    path('update_incident/<str:incident_id>/', views.update_incident),
    path('update_incident/', views.update_incident),
    path('create_incident/', views.create_incident),
    # path('user_register/', views.user_register),


]
