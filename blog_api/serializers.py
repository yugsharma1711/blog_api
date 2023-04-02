from rest_framework import serializers
from blog.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title','image', 'content', 'slug', 'status')
    def save(self, user):
        print(user)
        title = self.validated_data['title']
        image = self.validated_data['image']
        content = self.validated_data['content']
        slug = self.validated_data['slug']
        author = user
        status = self.validated_data['status']
        post = Post.objects.create(title = title,image = image, content= content, slug = slug, 
                                author = author, status = status)
        return post 