from django.urls import path
from accounts import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.userLogin, name='login'),
    path('register/', views.userRegister, name='register'),
    path('logout/', views.LogoutPage, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('reset/', views.resetpass, name='reset'),
]
