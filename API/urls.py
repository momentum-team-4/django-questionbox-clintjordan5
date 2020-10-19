from django.urls import path
from API import views
from rest_framework import routers

APIRouter = routers.DefaultRouter()
APIRouter.register('questions', views.question_list, basename='question')

urlpatterns = [
    path('API/', views.question_list),
    path('API/<int:pk>/', views.question_detail),
]

# need to fix primary keys. /API works, but questions/answers do not match. can view http://127.0.0.1:8000/API/7/, 0-6 not functioning