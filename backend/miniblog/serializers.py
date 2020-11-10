from rest_framework import serializers
from miniblog.models import BlogPost

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['id', 'author', 'title', 'body']

