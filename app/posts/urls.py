from django.urls import path
from .views import (PostRetrieveUpdateDestroyView,
                    PostCreateAPIView,
                    PostsLikedAPIView,
                    PostLikeAPIView)

urlpatterns = [
    path('new-post/', PostCreateAPIView.as_view(), name='post-new'),
    path('likes/', PostsLikedAPIView.as_view(), name='liked-posts'),
    path('<pk>/', PostRetrieveUpdateDestroyView.as_view(), name='post-retrieve-delete'),
    path('like/<post_id>', PostLikeAPIView.as_view(), name='like-unlike-post'),

]

