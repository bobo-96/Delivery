from rest_auth.views import LoginView
from django.urls import path
from rest_auth.registration.views import RegisterView

from user.views import UserView

urlpatterns = [
    path('signin/', LoginView.as_view(), name='rest_login'),
    path('signup/', UserView.as_view(), name='rest_register'),
    # path('user/<int:pk>', UserView.as_view({'get': 'retrieve', 'put': 'update'})),

]