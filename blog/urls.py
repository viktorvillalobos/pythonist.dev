from django.urls import path

from blog.views import PostListView, AboutView, PostDetailView

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
]
