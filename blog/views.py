from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UserSerializer, CategorySerializer, PostSerializer,CategoryPostSerializer
from .models import Category, Post
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.views import Response

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostCatViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().prefetch_related('category')
    serializer_class = CategoryPostSerializer


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user': user.pk,
            'email': user.email
        })