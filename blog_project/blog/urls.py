from django.urls import path
from .views import RegisterView, BlogPostListCreateView, BlogPostDetailView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    RegisterView,
    BlogPostListCreateView,
    BlogPostDetailView,
    home_view,
    post_detail_view,
    create_post_view
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('posts/', BlogPostListCreateView.as_view(), name='blogpost-list'),
    path('posts/<int:pk>/', BlogPostDetailView.as_view(), name='blogpost-detail'),
    path('', home_view, name='home'),
    path('create/', create_post_view, name='create-post'),
    path('posts/<int:pk>/view/', post_detail_view, name='post-detail'),
]
