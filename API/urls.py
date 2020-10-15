from django.urls import path
from API import views

urlpatterns = [
    path('API/', views.question_list),
    path('API/<int:pk>/', views.question_detail),
]

