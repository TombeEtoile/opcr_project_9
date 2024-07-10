from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator
from .models import Review, Ticket


class ReviewForm(forms.ModelForm):
    headline = forms.CharField(label='Titre', widget=forms.TextInput(attrs={'class': 'form-control'}))
    rating = forms.TypedChoiceField(
        label="Rating",
        coerce=int,
        widget=forms.RadioSelect,
        choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])
    body = forms.CharField(label='Commentaire',
                           required=False,
                           widget=forms.Textarea(attrs={'class': 'form-control'}))
    image = forms.ImageField(label='Image', required=False)

    class Meta:
        model = Review
        exclude = ['time_created', 'user', 'ticket']


class TicketForm(forms.ModelForm):
    headline = forms.CharField(label='Titre', widget=forms.TextInput(attrs={'class': 'form-control'}))
    body = forms.CharField(label='Commentaire',
                           required=False,
                           widget=forms.Textarea(attrs={'class': 'form-control'}))
    image = forms.ImageField(label='Image', required=False)

    class Meta:
        model = Ticket
        exclude = ['time_created', 'user']


class TicketAnswerForm(forms.ModelForm):
    headline = forms.CharField(label='Titre', widget=forms.TextInput(attrs={'class': 'form-control'}))
    rating = forms.TypedChoiceField(
        label="Rating",
        coerce=int,
        widget=forms.RadioSelect,
        choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])
    body = forms.CharField(label='Commentaire',
                           required=False,
                           widget=forms.Textarea(attrs={'class': 'form-control'}))
    image = forms.ImageField(label='Image', required=False)

    class Meta:
        model = Review
        exclude = ['time_created', 'user', 'ticket']
