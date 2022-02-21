from django.views.generic import ListView, DetailView
from .models import Post, Category

# NOTE: blog/templates/blog/post_list.html 찾음
class PostList(ListView):
    model = Post
    ordering = '-pk'
    # NOTE: template_name 을 직접 지정
    # template_name = 'blog/index.html'

    def get_context_data(self, **kwargs):
        # NOTE: post_list = Post.objects.all(); model = Post 의 default
        context = super(PostList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context

class PostDetail(DetailView):
    model = Post

'''
FBV 방식

from django.shortcuts import render

def index(request):
    posts = Post.objects.all().order_by('-pk')

    return render(
        request,
        'blog/index.html',
        {
            'posts': posts,
        }
    )

def single_post_page(request, pk):
    post = Post.objects.get(pk=pk)

    return render(
        request,
        'blog/single_post_page.html',
        {
            'post': post,
        }
    )
'''