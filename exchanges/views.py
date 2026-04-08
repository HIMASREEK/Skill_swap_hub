from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import ExchangeRequest, Review
from .forms import ReviewForm
from skills.models import Skill

@login_required
def exchange_list(request):
    requests_sent = ExchangeRequest.objects.filter(sender=request.user)
    requests_received = ExchangeRequest.objects.filter(receiver=request.user)

    context = {
        'requests': requests_sent | requests_received
    }
    return render(request, 'exchanges/request_list.html', context)

@login_required
def exchange_create(request, skill_id):
    receiver_skill = get_object_or_404(Skill, id=skill_id)

    if receiver_skill.user == request.user:
        return redirect('skill_list')

    sender_skills = Skill.objects.filter(user=request.user)

    if request.method == 'POST':
        sender_skill_id = request.POST.get('sender_skill')
        sender_skill = get_object_or_404(Skill, id=sender_skill_id, user=request.user)

        ExchangeRequest.objects.create(
            sender=request.user,
            receiver=receiver_skill.user,
            sender_skill=sender_skill,
            receiver_skill=receiver_skill
        )

        return redirect('exchange_list')

    return render(request, 'exchanges/request_create.html', {
        'receiver_skill': receiver_skill,
        'sender_skills': sender_skills
    })

@login_required
def request_detail(request, pk):
    req = get_object_or_404(ExchangeRequest, pk=pk)
    return render(request, 'exchanges/request_detail.html', {'request': req})

@login_required
def exchange_accept(request, pk):
    req = get_object_or_404(ExchangeRequest, pk=pk)
    if req.receiver == request.user and req.status == 'pending':
        req.status = 'accepted'
        req.save()
    return redirect('exchange_list')

@login_required
def exchange_reject(request, pk):
    req = get_object_or_404(ExchangeRequest, pk=pk)
    if req.receiver == request.user and req.status == 'pending':
        req.status = 'rejected'
        req.save()
    return redirect('exchange_list')

@login_required
def exchange_review(request, pk):
    req = get_object_or_404(ExchangeRequest, pk=pk)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.exchange = req
            review.reviewer = request.user
            review.save()
            return redirect('exchange_detail', pk=pk)
    else:
        form = ReviewForm()

    return render(request, 'exchanges/review_form.html', {'form': form})