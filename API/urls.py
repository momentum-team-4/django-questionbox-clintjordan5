from django.urls import path
from API import views

urlpatterns = [
    path('API/', views.API_list),
    path('API/<int:pk>/', views.API_detail),
]

