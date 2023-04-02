from django.urls import path
from .views import CustomUserClass

urlpatterns = [
    path('register/', CustomUserClass.as_view(), name ='create_user')
]
