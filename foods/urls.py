from django.urls import path

from .views import CommentDetail,CommentList,ReserveationDetail,ReserveationList,FoodDetail,FoodList


urlpatterns = [
    path('<int:pk>/', FoodDetail.as_view()),
    path('', FoodList.as_view()),
    path('CommentList/',CommentList.as_view()),
    path('<int:pk>/',CommentDetail.as_view()),
    path('Reserveation/',ReserveationList.as_view()),
    path('<int:pk>/',ReserveationDetail.as_view()),
  
    
]
