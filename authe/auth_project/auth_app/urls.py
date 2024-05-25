from django.urls import path 
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('register/',views.register_add,name='register'),
    path('login/',views.login_add,name='login'),
    path('logout/',views.logout_add,name='logout'),
    path('dashboard/',views.dashboard_add,name='dashboard')
]