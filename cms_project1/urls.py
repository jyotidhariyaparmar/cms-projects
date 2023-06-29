from django.contrib import admin
from django.urls import path

from django.urls import path

from cms_app.views import UserCreateAPIView, UserRetrieveUpdateDestroyAPIView, PostCreateAPIView, \
    PostRetrieveUpdateDestroyAPIView, LikeCreateAPIView, LikeRetrieveUpdateDestroyAPIView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('api/users/', UserCreateAPIView.as_view(), name='user-create'),
    path('api/users/<int:pk>/', UserRetrieveUpdateDestroyAPIView.as_view(), name='user-detail'),
    path('api/posts/', PostCreateAPIView.as_view(), name='post-create'),
    path('api/posts/<int:pk>/', PostRetrieveUpdateDestroyAPIView.as_view(), name='post-detail'),
    path('api/likes/', LikeCreateAPIView.as_view(), name='like-create'),
    path('api/likes/<int:pk>/', LikeRetrieveUpdateDestroyAPIView.as_view(), name='like-detail'),
]


