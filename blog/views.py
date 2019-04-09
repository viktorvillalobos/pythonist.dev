from django.views.generic import TemplateView, ListView, DetailView

from blog.models import Post


class PostListView(ListView):
    template_name = 'blog/home.html'
    queryset = Post.objects.filter(status=Post.PUBLISHED).order_by('-pk')
    paginate_by = 10


class AboutView(TemplateView):
    template_name = 'blog/about.html'

class PostDetailView(DetailView):
    model = Post

