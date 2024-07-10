from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterUserForm, UpdateUserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Subscription, UserFollows


# CRÉATION D'UTILISATEURS
def register(request):
    if request.user.is_authenticated:
        return redirect('reviews:index')
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reviews:index')
    else:
        form = RegisterUserForm()

    context = {
        'form': form
    }

    return render(request, 'accounts/register.html', context)


def logout_page(request):
    return render(request, 'accounts/logout_page.html')


# CRÉATION DU SYSTÈME D'ABONNEMENT
@login_required
def user_subscriptions(request):
    user = request.user
    subscriptions = UserFollows.objects.filter(user=user)
    subscribers = UserFollows.objects.filter(followed_user=user)

    context = {
        'subscriptions': subscriptions,
        'subscribers': subscribers,
    }
    return render(request, 'accounts/user_subscriptions.html', context)


@login_required
def follow_user(request, user_id):
    user_to_follow = get_object_or_404(User, id=user_id)
    if user_to_follow == request.user:
        messages.error(request, "Vous ne pouvez pas vous suivre vous-même.")
        return redirect('user_profile', user_id=user_id)

    follow, created = UserFollows.objects.get_or_create(user=request.user, followed_user=user_to_follow)
    if created:
        messages.success(request, f'Vous suivez maintenant {user_to_follow.username}.')
    else:
        messages.info(request, f'Vous suivez déjà {user_to_follow.username}.')
    return redirect('accounts:user_profile', user_id=user_id)


@login_required
def unfollow_user(request, user_id):
    user_to_unfollow = get_object_or_404(User, id=user_id)
    UserFollows.objects.filter(user=request.user, followed_user=user_to_unfollow).delete()
    messages.success(request, f'Vous ne suivez plus {user_to_unfollow.username}.')
    return redirect('accounts:user_profile', user_id=user_id)


@login_required
def user_profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    is_following = UserFollows.objects.filter(user=request.user, followed_user=user).exists()

    context = {
        'user_profile': user,
        'is_following': is_following,
    }
    return render(request, 'accounts/user_profile.html', context)


@login_required
def user_update(request):
    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:user_profile', user_id=request.user.id)
    else:
        form = UpdateUserForm(instance=request.user)

    context = {
        'form': form
    }
    return render(request, 'accounts/update_user.html', context)


# BARRE DE RECHERCHE
@login_required
def search_user(request):
    search = request.GET.get('search')
    users = User.objects.filter(username__icontains=search)
    context = {
        'search': search,
        'users': users,
    }
    return render(request, 'accounts/search_user.html', context)
