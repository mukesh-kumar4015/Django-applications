from django.urls import path
from api import views
from django.urls import path
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('user/', views.UserView.as_view(), name='user'),
    path('user/<int:user_id>/', views.UserView.as_view(), name='user'),
    path('incidents/', views.IncidentView.as_view(), name='incidents'),
    path('incidents/<str:incident_id>/', views.IncidentView.as_view(), name='incidents'),

]