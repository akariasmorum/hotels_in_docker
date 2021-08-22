from django.conf.urls import url
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

urlpatterns = [
    path('login/', LoginView.as_view(template_name='account/login.html'),  name="login"),
    path('logout/', LogoutView.as_view(template_name='account/logged_out.html'),  name="logout"),
    path('register/', views.register, name='register'),
]