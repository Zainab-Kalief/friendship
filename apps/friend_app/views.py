from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from ..user_app.models import User
from .models import Friend

# Create your views here.
def home(request):
    if 'user_id' in request.session:
        user = User.objects.get(id=request.session['user_id'])
        context = {'user': user, 'users': User.objects.all().order_by('-created_at')[:5]}
        return render(request, 'friend_app/home.html', context)
    else:
        return redirect('user:index')

def log_out(request):
    request.session.flush()
    return redirect('user:index')

def add_friend_page(request):
    if 'user_id' in request.session:
        user = User.objects.get(id=request.session['user_id'])
        context = {'users': User.objects.exclude(id__in=User.objects.filter(users__in=user.friends.all())).exclude(id=user.id).exclude(id__in=User.objects.filter(friends__in=user.users.all()))}
        return render(request, 'friend_app/add_friend.html', context)
    else:
        return redirect('user:index')

def add_friend(request, friend_id):
    user = User.objects.get(id=request.session['user_id'])
    friend = User.objects.get(id=friend_id)
    Friend.objects.create_friend(user=user, friend=friend)
    return redirect('friend:home')

def friend_list(request):
    if 'user_id' in request.session:
        user = User.objects.get(id=request.session['user_id'])
        friend_count = user.users.count() + user.friends.count()
        context = {'friends': user.friends.all(), 'friended': Friend.objects.all(), 'user': user, 'friend_count': friend_count}
        return render(request, 'friend_app/friends.html', context)
    else:
        return redirect('user:index')

def unfriend(request, friend_id):
    user = User.objects.get(id=request.session['user_id'])
    friend = User.objects.get(id=friend_id)
    if Friend.objects.filter(user=user, friend=friend):
        print Friend.objects.filter(user=user, friend=friend).delete()
    else:
        print Friend.objects.filter(user=friend, friend=user).delete()
    return redirect('friend:friend_list')
