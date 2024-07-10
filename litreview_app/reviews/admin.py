from django.contrib import admin

from .models import Review, Ticket


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('headline', 'rating', 'time_created')


class TicketAdmin(admin.ModelAdmin):
    list_display = ('user', 'headline', 'body', 'time_created')


admin.site.register(Review, ReviewAdmin)
admin.site.register(Ticket, TicketAdmin)
