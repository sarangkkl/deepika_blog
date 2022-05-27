from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.models import Profile, Follow
from post.models import Post
# Create your views here.

@login_required(login_url='accounts/login')
def index(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    # post = Post.objects.filter(author = profile)
    post = Post.objects.all()
    following = Follow.objects.filter(following=user).count()
    like_count =0
    dislike_count =0

    for x in post:
        like_count += x.like_count
        dislike_count += x.disliek_count
    context = {
        'profile': profile,
        'post': post,
        'following': following,
        'like_count': like_count,
        'dislike_count': dislike_count,
    }
    return render(request, 'home/index.html', context)
