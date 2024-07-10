from django.urls import path

from . import views

app_name = 'reviews'

urlpatterns = [
    path('', views.index, name='index'),

    path('review/<int:id>/', views.details, name='detail'),
    path('review/new_review/', views.new_review, name='new_review'),
    path('review/update_review/<int:id>/', views.update_review, name='update_review'),
    path('review/delete_review/<int:id>/', views.delete_review, name='delete_review'),
    path('review/user_reviews/', views.user_reviews, name='user_reviews'),

    path('review/ticket/new_ticket/', views.new_ticket, name='new_ticket'),
    path('review/ticket/<int:id>/', views.details_ticket, name='details_ticket'),
    path('review/update_ticket/<int:id>/', views.update_ticket, name='update_ticket'),
    path('review/delete_ticket/<int:id>/', views.delete_ticket, name='delete_ticket'),

    path('review/ticket/<int:id>/ticket_answer/', views.ticket_answer, name='ticket_answer'),
]
