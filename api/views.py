from django.shortcuts import render
from requests import Response

from .models import *
from .serializers import *
from .permissions import IsOwnerOrReadOnly

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly 

class UserList(ListAPIView):
     queryset = User.objects.all()
     serializer_class = UserSerializer

class UserDetail(RetrieveAPIView):
     queryset = User.objects.all()
     serializer_class = UserSerializer

class OrdersList(ListCreateAPIView):
     queryset = Orders.objects.all()
     serializer_class = OrdersSerializer
     permission_classes = [IsAuthenticated]

     def perform_create(self, seriaalizer):
          seriaalizer.save(owner = self.request.user)


class OrdersDetail(RetrieveUpdateDestroyAPIView):
     queryset = Orders.objects.all()
     serializer_class = OrdersSerializer
     permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class CategoriesList(ListAPIView):
     queryset = Categories.objects.all()
     serializer_class = CategoriesSerializer

