from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User


class Ticket(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    headline = models.fields.CharField(max_length=128, blank=True, null=True)
    body = models.fields.TextField(max_length=8192, blank=True, null=True)
    image = models.ImageField(upload_to='reviews_image/', height_field=None, width_field=None, null=True, blank=True)
    time_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return str(self.user)


class Review(models.Model):
    ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    headline = models.fields.CharField(max_length=128, blank=True, null=True)
    rating = models.fields.PositiveSmallIntegerField(
        blank=True, null=True,
        validators=[MinValueValidator(0), MaxValueValidator(5)])
    body = models.fields.TextField(max_length=8192, blank=True, null=True)
    image = models.ImageField(upload_to='reviews_image/', height_field=None, width_field=None, null=True, blank=True)
    time_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        # return self.ticket.user
        return self.headline
