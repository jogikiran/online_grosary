from django.urls import path
from .views import register_user_view, login_user_view, logout_user

urlpatterns = [
    path('register-users/', register_user_view),
    path('login-users/', login_user_view),
    path('logout-user/', logout_user),

]