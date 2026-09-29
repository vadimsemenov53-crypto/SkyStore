from django.urls import path
from users.apps import UsersConfig
from users.views import UserCreateView, email_verification, UserLoginView, UserDetailView, UserUpdateView
from django.contrib.auth.views import LogoutView

app_name = UsersConfig.name

urlpatterns = [
    path('login/', UserLoginView.as_view(next_page='users:detail'), name='login'),
    path('logout/', LogoutView.as_view(next_page='catalog:home'), name='logout'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('email-confirm/<str:token>/', email_verification, name='email-confirm'),
    path('detail/', UserDetailView.as_view(), name='detail'),
    path('update/', UserUpdateView.as_view(), name='update')
]
