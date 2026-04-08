from django.shortcuts import render, redirect, get_object_or_404
from .models import Skill
from .forms import SkillForm
from django.contrib.auth.decorators import login_required

@login_required
def skill_list(request):
    skills = Skill.objects.exclude(user=request.user)
    my_skills = Skill.objects.filter(user=request.user)
    return render(request, 'skills/skill_list.html', {
        'skills': skills,
        'my_skills': my_skills
    })

@login_required
def skill_add(request):
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.user = request.user
            skill.save()
            return redirect('skill_list')
    else:
        form = SkillForm()
    return render(request, 'skills/skill_add.html', {'form': form})

@login_required
def skill_edit(request, pk):
    skill = get_object_or_404(Skill, pk=pk, user=request.user)
    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            return redirect('skill_list')
    else:
        form = SkillForm(instance=skill)
    return render(request, 'skills/skill_edit.html', {'form': form})