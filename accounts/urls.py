from django.urls import path

from .views import SignUp,LogIn

app_name = 'accounts'

urlpatterns = [
    path('login/',LogIn, name='login'),
    path('signup/',SignUp, name='signup'),
]