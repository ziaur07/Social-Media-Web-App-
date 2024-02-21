
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("newPost", views.newPost, name="newPost"),
    path('allPosts', views.allPosts, name='allPosts'),
    path('profile/<str:username>', views.profile, name='profile'),
    path('follow/<str:username>', views.follow, name='follow'),
    path('all_users', views.all_users, name='all_users'),
    path('following', views.following_posts, name='following_posts'),
    path('like_post', views.like_post, name='like_post'),
    path('edit_post', views.edit_post, name='edit_post')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)