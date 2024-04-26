from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from products.views import OrderCreateAPIView, LogoutView, TaskListCreateAPIView, TaskRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('api/orders/', OrderCreateAPIView.as_view(), name='order-create'),
    path('api/logout/', LogoutView.as_view(), name='logout'),
    path('tasks/', TaskListCreateAPIView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDestroyAPIView.as_view(), name='task-retrieve-update-destroy')
]
