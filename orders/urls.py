from django.urls import path

from orders.views import OrderView, StatusView

urlpatterns = [
    path('', OrderView.as_view({'get': 'list'})),
    path('create/', OrderView.as_view({'post': 'create'})),
    path('<int:pk>/', OrderView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('status/<int:pk>', StatusView.as_view({'get': 'retrieve', 'put': 'update'})),

]