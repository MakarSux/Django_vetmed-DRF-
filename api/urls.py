from django.urls import path
from .views import *


urlpatterns = [
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
    path('orders/', OrdersList.as_view()),
    path('orders/<int:pk>/', OrdersDetail.as_view()),
    path('categories/', CategoriesList.as_view()),
]
