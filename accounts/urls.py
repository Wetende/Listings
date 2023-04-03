from django.urls import path

from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('profile', views.profile, name='uProfile'),
    path('mProperties/<int:user_id>/', views.mProperties, name='mProperties'),
    path('favourite_properties/<int:user_id>/', views.favourite_properties, name='fProperties'),
    path('change_password', views.change_password, name='cPassword'),
    
   
]
