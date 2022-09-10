from django.shortcuts import render
from rest_framework import generics, permissions
from .models import  Food,Comment,Reserveation
from .serializers import Foodserializer,Commentserializer,Reserveationserializer
# Create your views here.



class ReserveationList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset =Reserveation.objects.all()
    serializer_class =Reserveationserializer 

class ReserveationDetail(generics.RetrieveDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Reserveation.objects.all()
    serializer_class = Foodserializer

class FoodList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset =Food.objects.all()
    serializer_class =Foodserializer

class FoodDetail(generics.RetrieveDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Food.objects.all()
    serializer_class = Reserveationserializer

class CommentList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset =Comment.objects.all()
    serializer_class =Commentserializer

class CommentDetail(generics.RetrieveDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Comment.objects.all()
    serializer_class = Commentserializer