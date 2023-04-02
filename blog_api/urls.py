from django.urls import path
from . import views

app_name = 'blog_api'

urlpatterns = [
    path('createblog/', views.PostList.as_view(), name = 'listcreate'),
    path('getblog/<int:pk>/', views.PostDetail.as_view(), name='detailcreate'),
    path('getallblog/', views.GetAllpost.as_view()),
    path('deleteblog/<int:pk>', views.DeletePost.as_view())
]