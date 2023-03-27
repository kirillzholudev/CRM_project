from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import AddLeadForm
from .models import Lead


@login_required
def leads_list(request):
	leads = Lead.objects.filter(created_by=request.user)

	return render(request, 'lead/leads_list.html', {
		'leads': leads
	})


@login_required
def leads_detail(request, pk):
	lead = get_object_or_404(Lead, created_by=request.user, pk=pk)

	return render(request, 'lead/leads_detail.html', {
		'lead': lead
	})


@login_required
def add_lead(request):
	if request.method == 'POST':
		form = AddLeadForm(request.POST)

		if form.is_valid():
			lead = form.save(commit=False)
			lead.created_by = request.user
			lead.save()

			return redirect('dashboard')
	else:
		form = AddLeadForm()

	return render(request, 'lead/add_lead.html', {
		'form': form
	})
