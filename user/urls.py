from rest_auth.views import LoginView
from django.urls import path
from rest_auth.registration.views import RegisterView

urlpatterns = [
    path('signin/', LoginView.as_view(), name='rest_login'),
    path('signup/', RegisterView.as_view(), name='rest_register')

]