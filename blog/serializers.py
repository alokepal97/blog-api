from django.contrib.auth.models import User
from django.db.models import fields
from rest_framework import serializers
from .models import Category, Post

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'password', 'is_staff']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    url = serializers.URLField(read_only = True)
    class Meta:
        model = Post
        fields = '__all__'

class CategoryPostSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(source='insdate',format="%d %b, %Y")
    
    category = CategorySerializer()
    user = UserSerializer()
    class Meta:
        model = Post
        fields = ['id','title', 'content', 'category', 'user', 'url', 'date']