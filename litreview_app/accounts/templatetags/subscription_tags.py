from django import template
from ..models import Subscription

register = template.Library()


@register.filter
def is_subscribed_to(user, user_to_check):
    return Subscription.objects.filter(subscriber=user, subscribed_to=user_to_check).exists()
