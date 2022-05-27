from django.shortcuts import render,redirect
from django.contrib import messages
from . models import Post,Comment
from accounts.models import Profile
from django.db.models import Q
# Create your views here.


def handle_create_post(request):
    if request.method == "POST":
        user = request.user
        profile = Profile.objects.get(user=user)
        message = request.POST.get("message")
        title = request.POST.get("title")
        file = request.FILES.get("image")
        x = Post.objects.create(content=message,image=file,title=title,author=profile)
        x.save()
        messages.error(request,'The Tweet has been created')
        return redirect('/')
    else:
        messages.error(request,'You can not hit me baby')
        return redirect('/')

def handle_search_post(request):
    if request.method == "POST":
        search = request.POST.get("search")
        post = Post.objects.filter(Q(title__icontains=search) | Q(content__icontains=search))
        count = post.count()
        context = {
            'post': post,
            'count': count,
        }
        return render(request,'home/searchResult.html',context)
    else:
        return redirect('/')

def article(request,id):
    post = Post.objects.get(id=id)
    comments = Comment.objects.filter(post=post)
    count = comments.count()
    context = {
        'post': post,
        'comments': comments,
        'count': count,
    }
    return render(request,'post/article_detail.html',context)

def save_comment(request,id):
    if request.method == "POST":
        user = request.user
        profile = Profile.objects.get(user=user)
        message = request.POST.get("message")
        post = Post.objects.get(id=id)
        x = Comment.objects.create(content=message,author=profile,post=post)
        x.save()
        messages.error(request,'comment has been created')
        return redirect('/post/article_detail/'+str(id))
    else:
        messages.error(request,'You can not hit me baby')
        return redirect('/post/article_detail/'+str(id))

def like(request,id):
    post = Post.objects.get(id=id)
    post.like_count += 1
    post.save()
    return redirect('/')

def dislike(request,id):
    post = Post.objects.get(id=id)
    post.disliek_count += 1
    post.save()
    return redirect('/')
