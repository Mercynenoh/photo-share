from django.shortcuts import render, redirect,get_object_or_404
from django.http  import HttpResponse, Http404
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from pictures.models import Post, Profile, FollowersCount
from django import template
from django.db import models
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin





def search_results(request):

    if 'post' in request.GET and request.GET["post"]:
        search_term = request.GET.get("post")
        searched_posts = Post.search_by_author(search_term)
        message = f"{search_term}"

        return render(request, 'pictures/search.html',{"message":message,"posts": searched_posts})

    else:
        message = "Ooops we can't find that!!"
        return render(request, 'pictures/search.html',{"message":message})

def viewPhoto(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        value = request.POST['value']
        comments = request.POST['comments']
        if value == 'comments':
            comments.save()
    return render(request, 'pictures/image.html', {'post':post})

def image_list(request):
    posts = models.Post.objects.all()
    return render(request, "pictures/post_list.html", {'post':post})


def followers_count(request):
    if request.method == 'POST':
        value = request.POST['value']
        user = request.POST['user']
        follower =request.POST['follower']
        if value == 'follow':
            followers_cnt = FollowersCount.objects.create(follower=follower, user=user)
            followers_cnt.save()
        return redirect('/?user='+user)



# def image_view(request, pk):
#         post = Post.objects.get(id=pk)
#         short_description = image.description
#         return render(request, "image.html", {'post':post})


class ImageList(LoginRequiredMixin,ListView):
    model = Post
    template_name = 'pictures/post_list.html'

    def get_queryset(self):
        return Post.objects.all()

class ProfileList( ListView):
    model = Profile
    template_name = 'pictures/profile_list.html'

    def get_queryset(self):
        return Profile.objects.all()

def gallery(request):
    profile= profile.request.GET.get('profile')
    profiles = Profile.objects.all()
    authors = Author.objects.all()
    photos = Photo.objects.all()
    posts = models.Posts.objects.all()
    current_user= request.GET.get('user')
    logged_in_user=request.user.username 
    user_followers = FollowersCount.objects.filter(author=current_user)
    

    context = {'profiles': profiles,'photos':photos, ' current_user': current_user}

    return render(request, 'pictures/post_list.html', context)


class ImageCreate(LoginRequiredMixin, CreateView):
    login_url = '/accounts/login'
    # redirect_field_name = '/accounts/login'
    model = Post
    fields = ['image', 'imagename', 'caption', 'author', 'profile', 'location', 'comments']
    success_url = '/'

class ItemUpdateView(UpdateView):
    model = Post

  

    