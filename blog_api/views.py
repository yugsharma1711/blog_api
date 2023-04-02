from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.views import View
from rest_framework.parsers import MultiPartParser, FormParser
class PostList(generics.CreateAPIView):
    permission_classes = [IsAuthenticated,]
    parser_classes = [MultiPartParser, FormParser]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    def post(self, request):
        user = self.request.user
        serializer = PostSerializer(data = self.request.data)
        if serializer.is_valid(raise_exception=True):       
            serializer.save(user)
        return Response(serializer.data)


class PostDetail(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
class GetAllpost(generics.ListAPIView):
    #permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    

class DeletePost(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer