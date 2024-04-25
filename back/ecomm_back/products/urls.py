from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from .views import OrderCreateAPIView, LogoutView

urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('api/orders/', OrderCreateAPIView.as_view(), name='order-create'),
    path('api/logout/', LogoutView.as_view(), name='logout')
]
