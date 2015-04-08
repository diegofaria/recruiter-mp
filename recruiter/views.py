from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Candidate
from .forms import CandidateForm
from .engine import NewCandidateEngine

def candidate_list(request):
    candidates = Candidate.objects.all().order_by('published_date')
    return render(request, 'recruiter/candidates_list.html', {'candidates': candidates})

def candidate_detail(request, pk):
	candidate = get_object_or_404(Candidate, pk=pk)
	return render(request, 'recruiter/candidate_detail.html', {'candidate': candidate})

def candidate_finish(request, pk):
	candidate = get_object_or_404(Candidate, pk=pk)
	return render(request, 'recruiter/candidate_finish.html', {'candidate': candidate})

def candidate_new(request):
	if request.method == "POST":
		form = CandidateForm(request.POST)
		if form.is_valid():
			candidate = form.save(commit=False)
			new_candidate_engine = NewCandidateEngine()
			candidate = new_candidate_engine.create(candidate)
			return redirect('recruiter.views.candidate_finish', pk=candidate.pk)
	else: 
		form = CandidateForm()
	return render(request,'recruiter/candidate_edit.html', {'form': form})   		

def candidate_edit(request, pk):
	candidate = get_object_or_404(Candidate, pk=pk)
	if request.method == "POST":
		form = CandidateForm(request.POST, instance=candidate)
		if form.is_valid():
			candidate = form.save(commit=False)
			new_candidate_engine = NewCandidateEngine()
			candidate = new_candidate_engine.create(candidate)
			return redirect('recruiter.views.candidate_detail', pk=candidate.pk)
	else: 
		form = CandidateForm(instance=candidate)
	return render(request,'recruiter/candidate_edit.html', {'form': form}) 