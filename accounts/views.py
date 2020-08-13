from django.contrib import auth
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from vibin_app.models import Friend



def register(request):
  if request.method == "POST":
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    username_form = request.POST['username']
    email_form = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']

    if password == password2:
      if User.objects.filter(username=username_form).exists():
        context = {'error': 'Username is already taken.'}
        return render(request, 'register.html', context)
      else:
        if User.objects.filter(email=email_form).exists():
          context = {'error':'That email already exists.'}
          return render(request, 'register.html', context)
        else: 
          user = User.objects.create_user(
            username=username_form, 
            email=email_form, 
            password=password, 
            first_name=first_name, 
            last_name=last_name)
          user.save()
          return redirect('artist_list')
    else:
        context = {'error': 'Password do not match'}
        return render(request, 'register.html', context)
  else: 
      return render(request, 'register.html')



def login(request):
  if request.method == 'POST':
    username_form = request.POST['username']
    password_form = request.POST['password']

    user = auth.authenticate(username=username_form, password=password_form)
    if user is not None:
      auth.login(request, user)
      return redirect('profile')
    else:
      context = {'error': 'Invalid Credentials'}
      return render(request, 'login.html', context)
  else:
    return render(request, 'login.html')




def logout(request):
  auth.logout(request)
  return redirect('artist_list')


def profile(request):
  artists = Artist.objects.filter(user=request.user)
  users = User.objects.all()
  friend = Friend.objects.get(current_user=request.user)
  friends = friend.users.all()
  context = {'artists':artists, 'users': users, 'friends': friends}
  return render(request, 'profile.html', context)

# def profile(request):
#   artists = Artist.objects.filter(user=request.user)
#   users = User.objects.all()
#   context = {'artists':artists, 'users': users}
#   return render(request, 'profile.html', context)

# def profile(request, pk):
#   user = User.objects.get(id=pk)
#   friend = Friend.objects.get(current_user=request.user)
#   friends = friend.users.all()
#   context = {'user': user, 'friends': friends}
#   return render(request, 'profile.html', context)


def user_list(request):
  users = User.objects.all()
  context = {'users': users}
  return render(request, 'user_list.html', context)



def user_profile(request, pk):
  user = User.objects.get(id=pk)
  users = User.objects.all()
  friend = Friend.objects.get(current_user=request.user)
  friends = friend.users.all()
  context = {'user': user, 'friends': friends, 'users': users}
  return render(request, 'profile.html', context)
  

def their_friends(request, pk):
  user = User.objects.get(id=pk)
  users = User.objects.all()
  friend = Friend.objects.get(current_user=request.user)
  friends = friend.users.all()
  their_friends = Friend.objects.get(id=pk)
  their_friends_list= their_friends.users.all()
  context = {'user': user, 'friends': friends, 'users': users, 'their_friends_list': their_friends_list}
  return render(request, 'their_friends.html', context)


# def friend(request, pk):
#   if request.method == 'POST':
#     user = User.objects.get(id=pk)
#     friends = []
#     friends.append(user)
#     context = {'friends': friends}
#   return render(request, 'profile.html', context)


def remove_friends(request, pk):
  friend = User.objects.get(pk=pk)
  Friend.lose_friend(request.user, friend)
  return render(request, 'profile.html')


def change_friends(request, pk):
  friend = User.objects.get(pk=pk)
  Friend.make_friend(request.user, friend)
  return render(request, 'profile.html')


def friend_list(request, pk):
  user = User.objects.get(id=pk)
  users = User.objects.all()
  friend = Friend.objects.get(current_user=request.user)
  friends = friend.users.all()
  context = {'user': user, 'friends': friends, 'users': users}
  return render(request, 'friend_list.html', context)


def add_remove_friends(request, operation, pk):
  friend = User.objects.get(pk=pk)
  if operation == 'add':
    Friend.make_friend(request.user, friend)
  elif operation == 'remove':
    Friend.lose_friend(request.user, friend)
  return redirect('profile')