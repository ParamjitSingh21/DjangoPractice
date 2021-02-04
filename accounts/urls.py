from django.urls import path
from django.contrib.auth import views
from .views import frontpage,SignUp#,LogIn,
from .forms import *

app_name = 'accounts'

urlpatterns = [
    # path('login/',LogIn, name='login'),
    path('signup/',SignUp, name='signup'),
    path('', frontpage, name="frontpage"),
    path('login/', views.LoginView.as_view(template_name="login.html", authentication_form=UserLoginForm), name="login"),
    path('logout/', views.LogoutView.as_view(), name="logout"),
]