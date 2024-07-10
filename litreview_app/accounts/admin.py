from django.contrib import admin
from .models import Subscription, UserFollows


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('subscriber', 'subscribed_to', 'created_at')
    search_fields = ('subscriber__username', 'subscribed_to__username')


class UserFollowsAdmin(admin.ModelAdmin):
    list_display = ('user', 'followed_user')
    search_fields = ('user__username', 'followed_user__username')


admin.site.register(Subscription)
admin.site.register(UserFollows, UserFollowsAdmin)
