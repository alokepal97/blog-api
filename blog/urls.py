from django.urls import path ,include
from rest_framework import routers
from .views import UserViewSet, CategoryViewSet, PostViewSet, PostCatViewSet, CustomAuthToken

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'post', PostViewSet, basename='post')
router.register(r'post-cat', PostCatViewSet, basename='post-cat')

urlpatterns = [
    path('api-token-auth/', CustomAuthToken.as_view()),
    path('',  include(router.urls))
]