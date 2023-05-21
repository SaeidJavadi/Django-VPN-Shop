from django.urls import path
from payment import views

app_name = 'payment'
urlpatterns = [
    path('pay/', views.send_request, name='pay'),
    path('verify/', views.verify, name='verify'),
]
