from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import BadRequest
from django.contrib.auth.decorators import login_required
from .models import Review, Ticket
from .forms import ReviewForm, TicketForm, TicketAnswerForm
from django.http import Http404
from django.core.paginator import Paginator


@login_required
def index(request):
    reviews = Review.objects.order_by('-time_created').all()
    reviews_number = reviews.count()
    tickets = Ticket.objects.order_by('-time_created').all()
    tickets_number = tickets.count()
    combined = sorted(
        list(reviews) + list(tickets),
        key=lambda x: x.time_created if isinstance(x, Ticket) else x.time_created,
        reverse=True
    )
    paginator = Paginator(combined, 5)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)
    context = {
        'items': page_object,
        'reviews': reviews,
        'tickets': tickets,
        'reviews_number': reviews_number,
        'tickets_number': tickets_number,
    }
    return render(request, 'reviews/index.html', context)


@login_required
def details(request, id):
    review = Review.objects.get(id=id)
    context = {
        'review': review
    }
    return render(request, 'reviews/details.html', context)


@login_required
def new_review(request):
    form = ReviewForm()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('reviews:index')
    context = {
        'form': form
    }
    return render(request, 'reviews/new_review.html', context)


@login_required
def update_review(request, id):
    review = Review.objects.get(id=id)
    if review.user == request.user:
        if request.method == 'POST':
            review_form = ReviewForm(request.POST, request.FILES, instance=review)
            if review_form.is_valid():
                review_form.save()
                return redirect('reviews:index')
        else:
            review_form = ReviewForm(instance=review)
    else:
        raise Http404

    context = {
        'review_form': review_form,
        'review': review,
    }
    return render(request, 'reviews/update_review.html', context)


@login_required
def delete_review(request, id):
    review = Review.objects.get(id=id)
    if review.user == request.user:
        review.delete()
        return redirect('reviews:index')
    else:
        raise Http404


@login_required
def user_reviews(request):
    reviews = Review.objects.filter(user=request.user).order_by('-time_created')
    reviews_number = reviews.count()
    context = {
        'reviews': reviews,
        'reviews_number': reviews_number
    }
    return render(request, 'reviews/user_reviews.html', context)


@login_required
def details_ticket(request, id):
    ticket = Ticket.objects.get(id=id)
    context = {
        'ticket': ticket
    }
    return render(request, 'reviews/details_ticket.html', context)


@login_required
def new_ticket(request):
    ticket_form = TicketForm()
    if request.method == 'POST':
        ticket_form = TicketForm(request.POST, request.FILES)
        if ticket_form.is_valid():
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            if ticket_form.cleaned_data['image']:
                ticket.image = ticket_form.cleaned_data['image']
            ticket.save()
            return redirect('reviews:index')
    context = {
        'ticket_form': ticket_form
    }
    return render(request, 'reviews/new_ticket.html', context)


@login_required
def ticket_answer(request, id):
    ticket = Ticket.objects.get(id=id)
    if request.method == 'POST':
        review_form = TicketAnswerForm(request.POST, request.FILES)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.ticket = ticket  # Associer le ticket à la critique
            review.save()
            return redirect('reviews:index')
    else:
        review_form = ReviewForm()
    context = {
        'ticket': ticket,
        'review_form': review_form,
    }
    return render(request, 'reviews/ticket_answer.html', context)


@login_required
def update_ticket(request, id):
    ticket = Ticket.objects.get(id=id)
    if ticket.user == request.user:
        if request.method == 'POST':
            form = TicketForm(request.POST, request.FILES, instance=ticket)
            if form.is_valid():
                form.save()
                return redirect('reviews:index')
        else:
            form = TicketForm(instance=ticket)
    else:
        raise Http404

    context = {
        'form': form,
        'ticket': ticket,
    }
    return render(request, 'reviews/update_ticket.html', context)


@login_required
def delete_ticket(request, id):
    ticket = Ticket.objects.get(id=id)
    if ticket.user == request.user:
        ticket.delete()
        return redirect('reviews:index')
    else:
        raise Http404
