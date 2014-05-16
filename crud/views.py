from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render_to_response

from crud.models import Athlete
from crud.forms import AthleteForm


def index(request):
	all_athletes = Athlete.objects.all()
	template = loader.get_template('crud/index.html')
	context = RequestContext(request, {
		'all_athletes' : all_athletes,
		})
	return HttpResponse(template.render(context))

def detail(request, athlete_id):
	# Find the athlete from the db using the id passed with the request
	athlete = Athlete.objects.get(pk=athlete_id)
	template = loader.get_template('crud/detail.html')
	context = RequestContext(request, {
		'athlete' : athlete,
		})
	return HttpResponse(template.render(context))

def add(request):
	context = RequestContext(request)

	if request.method == 'POST':
		form = AthleteForm(request.POST)

		if form.is_valid():
			form.save(commit = True)
			return index(request)
		else:
			print form.errors
	
	else:
		form = AthleteForm()
	return render_to_response('crud/add.html', { 'form' : form }, context)