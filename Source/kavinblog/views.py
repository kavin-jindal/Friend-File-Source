from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator, EmptyPage,\
                                  PageNotAnInteger
from .models import Post, Category, Comment
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .forms import PostForm, CommentForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
# Create your views here.
'''
def home(request):
	return render(request, 'home.html', {})
	'''


def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-', ' '))
    return render(request, 'categories.html', {
        'cats': cats.title().replace('-', ' '),
        'category_posts': category_posts
    })


def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse_lazy('article_detail', args=[str(pk)]))


def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'category_list.html',
                  {'cat_menu_list': cat_menu_list})


class HomeView(ListView):
    model = Post
    cats = Category.objects.all()
    template_name = 'home.html'
    #ordering = ('-post_date')[0:3]
    queryset = Post.objects.order_by('-post_date')[:20]

    #posts = Post.objects.filter(published=True).order_by('-post_date')[0:3]
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'new.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleDetailView,
                        self).get_context_data(*args, **kwargs)
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True

        context["cat_menu"] = cat_menu
        context['total_likes'] = total_likes
        context['liked'] = liked
        return context


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_blog.html'
    #fields = '__all__'


class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comment.html'
    success_url = reverse_lazy('home')
    #fields = '__all__'


class UpdatePost(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'update_post.html'


    #fields = ['title', 'body']
class DeveloperView(ListView):
    model = Post
    template_name = 'dev.html'


class AllPostView(ListView):
    model = Post
    template_name = 'all_post.html'
    queryset = Post.objects.order_by('-post_date')


class BlogView(ListView):
    model = Post
    template_name = 'blog.html'


class TechView(ListView):
    model = Post
    template_name = 'tech.html'


class LinuxView(ListView):
    model = Post
    template_name = 'linux.html'


class ValorantView(ListView):
    model = Post
    template_name = 'valorant.html'


class CODView(ListView):
    model = Post
    template_name = 'cod.html'


class HackView(ListView):
    model = Post
    template_name = 'hack.html'


class PythonView(ListView):
    model = Post
    template_name = 'python.html'


class CyberView(ListView):
    model = Post
    template_name = 'cyber.html'


class GamingView(ListView):
    model = Post
    template_name = 'gaming.html'


class PenView(ListView):
    model = Post
    template_name = 'pen.html'


class UpView(ListView):
    model = Post
    template_name = 'update.html'


class AboutView(ListView):
    model = Post
    template_name = 'about.html'


class DeletePost(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('home')


class AddCateGoryView(CreateView):
    model = Category
    #form_class = PostForm
    template_name = 'add_category.html'
    fields = '__all__'
