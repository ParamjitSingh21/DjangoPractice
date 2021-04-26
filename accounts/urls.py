from django.urls import path
from django.contrib.auth import views
from .views import frontpage,SignUp#,LogIn,
from .forms import UserLoginForm, ResetPasswordForm, NewPasswordForm

app_name = 'accounts'

urlpatterns = [
    
    path('signup/',SignUp, name='signup'),
    path('', frontpage, name="frontpage"),
    path('login/', views.LoginView.as_view(template_name="login.html", authentication_form=UserLoginForm), name="login"),
    path('logout/', views.LogoutView.as_view(), name="logout"),
    path('password-reset/', views.PasswordResetView.as_view(template_name="reset_password.html", form_class=ResetPasswordForm), name="password-reset"),
]