from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import LoginForm
from . import views


app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html',
                                                redirect_authenticated_user=True,
                                                authentication_form=LoginForm),
         name='login'),
    path('logout_page/logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'),
         name='logout'),
    path('logout_page/', views.logout_page, name='logout_page'),
    path('register/', views.register, name='register'),

    path('follow/<int:user_id>/', views.follow_user, name='follow_user'),
    path('unfollow/<int:user_id>/', views.unfollow_user, name='unfollow_user'),

    path('user_subscriptions/', views.user_subscriptions, name='user_subscriptions'),
    path('user_profile/<int:user_id>/', views.user_profile, name='user_profile'),
    path('user_update/', views.user_update, name='user_update'),
    path('search_user/', views.search_user, name='search_user'),
]
