from django.urls import path
# . import views
from .views import HomeView, ArticleDetailView,AllPostView,BlogView,LinuxView,ValorantView,LikeView,PythonView,PenView,CODView,CategoryListView,GamingView, AddPostView,CyberView, UpdatePost,TechView,HackView, DeletePost,AddCateGoryView, CategoryView, DeveloperView, UpView, AboutView,AddCommentView
urlpatterns = [
    #path('', views.home, name='home'),
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('article/<int:pk>/comment', AddCommentView.as_view(), name='add_comment'),

    path('add_cat/', AddCateGoryView.as_view(), name='add_cat'),
    path('article/edit/<int:pk>', UpdatePost.as_view(), name='update_post'),
    path('article/<int:pk>/delete', DeletePost.as_view(), name='delete'),
    path('like/<int:pk>', LikeView, name='like_post'),
    path('category-list/', CategoryListView, name='category_list'),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('dev/', DeveloperView.as_view(), name='developer'),
    path('devblog/', UpView.as_view(), name='devblog'),
    path('about/', AboutView.as_view(), name='about'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('tech/', TechView.as_view(), name='tech'),
    path('python/', PythonView.as_view(), name='python'),
    path('linux/', LinuxView.as_view(), name='linux'),
	path('hacking/', HackView.as_view(), name='hacking'),
	path('cyber/', CyberView.as_view(), name='cyber'),
	path('pentesting/', PenView.as_view(), name='pentesting'),
	path('gaming/', GamingView.as_view(), name='gaming'),
	path('cod/', CODView.as_view(), name='cod'),
    path('valorant/', ValorantView.as_view(), name='valo'),
    path('all_posts/', AllPostView.as_view(), name='all_blogs'),





]
