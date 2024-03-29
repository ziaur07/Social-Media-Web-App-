from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from .models import User, Post, UserProfile

import json


def index(request):
    return render(request, "network/index.html")



@login_required
def newPost (request):
    if request.method == 'POST': 
        print(request.FILES) # If the form has been submitted...
        content = request.POST.get('content')
        image = request.FILES.get('image') 
        user = User.objects.get(pk=request.user.id)
        post = Post(content=content, user=user, image=image )
        post.save()
        return HttpResponseRedirect(reverse(index))
    

def all_users(request):
    users = User.objects.all()
    return render(request, 'all_users.html', {'users': users})
    


#@login_required
#def allPosts(request):
    posts = Post.objects.all().order_by('-post_date')
    return render(request, 'all_posts.html', {'posts': posts})

@login_required
def allPosts(request):
    posts_list = Post.objects.all().order_by('-post_date')
    paginator = Paginator(posts_list, 10)  # Show 10 posts per page

    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    return render(request, 'all_posts.html', {'posts': posts})


@login_required
def profile(request, username):
    user = User.objects.get(username=username)
    
    user_profile = UserProfile.objects.get(user=user)
    followers_count = UserProfile.objects.filter(following=user).count()
    posts = Post.objects.filter(user=user).order_by('-post_date')
    return render(request, 'profile.html', {'user_profile': user_profile, 'posts': posts, 'followers_count': followers_count})


@login_required
def follow(request, username):
    target = get_object_or_404(User, username=username)
    if request.user == target:
        # Users can't follow themselves
        return redirect('profile', username=username)

    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if target in user_profile.following.all():
        # If the current user is already following the target user, unfollow them
        user_profile.following.remove(target)
    else:
        # If the current user is not following the target user, follow them
        user_profile.following.add(target)

    return redirect('profile', username=username)



#@login_required
#def following_posts(request):
    user_profile = UserProfile.objects.get(user=request.user)
    following_users = user_profile.following.all()
    posts = Post.objects.filter(user__in=following_users)
    return render(request, 'following_posts.html', {'posts': posts}) 
@login_required
def following_posts(request):
    user_profile = UserProfile.objects.get(user=request.user)
    following_users = user_profile.following.all()
    posts_list = Post.objects.filter(user__in=following_users)
    
    paginator = Paginator(posts_list, 10)  # Show 10 posts per page

    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    return render(request, 'following_posts.html', {'posts': posts})


@csrf_exempt
@login_required
def edit_post(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        post_id = data.get('post_id')
        new_content = data.get('content')
        post = Post.objects.get(id=post_id)
        if request.user != post.user:
            return JsonResponse({"error": "You are not authorized to edit this post."}, status=403)
        post.content = new_content
        post.save()
        return JsonResponse({"message": "Post updated successfully."}, status=201)

@csrf_exempt
@login_required
def like_post(request):
    if request.method == 'POST':
        post_id = json.loads(request.body).get('post_id')
        post = Post.objects.get(id=post_id)
        like_count = post.toggle_like(request.user)
        return JsonResponse({'like_count': like_count}, status=200)

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
            UserProfile.objects.create(user=user)
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")



       
       

       
           
           
           
           
   