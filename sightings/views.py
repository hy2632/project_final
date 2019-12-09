from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.

from .models import Squirrel
from .forms import SquirrelForm #Build a Form


def index(request):
	sightings = Squirrel.objects.all().order_by('Unique_Squirrel_ID')
	context={'sightings':sightings}
	return render(request, 'sightings/index.html',context)
	
def update(request,sqr_id):
	sqr = Squirrel.objects.get(Unique_Squirrel_ID=sqr_id)
	if request.method =='POST':
		form = SquirrelForm(request.POST, instance=sqr)
		if form.is_valid():
			form.save()
			return redirect(f'/sightings/')
	else:
		form = SquirrelForm(instance=sqr)

	context={
		'form':form,
	}
	return render(request, 'sightings/update.html',context)

def add(request):
	if request.method == 'POST':
		form = SquirrelForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect(f'/sightings/')
	else:
		form = SquirrelForm

	context={
		'form':form,
	}
	return render(request, 'sightings/add.html', context)

def stats(request):
	squirrel_count = Squirrel.objects.all().count()

	Running_True=0
	for i in Squirrel.objects.values_list('Running'):
		if 'true' in i:
			Running_True+=1

	Chasing_True=0
	for i in Squirrel.objects.values_list('Chasing'):
		if 'true' in i:
			Chasing_True+=1

	Climbing_True=0
	for i in Squirrel.objects.values_list('Climbing'):
		if 'true' in i:
			Climbing_True+=1

	Eating_True=0
	for i in Squirrel.objects.values_list('Eating'):
		if 'true' in i:
			Eating_True+=1

	Foraging_True=0
	for i in Squirrel.objects.values_list('Foraging'):
		if 'true' in i:
			Foraging_True+=1


	context={
			'squirrel_count':squirrel_count,
			'Running_True':Running_True,
			'Chasing_True':Chasing_True,
			'Climbing_True':Climbing_True,
			'Eating_True':Eating_True,
			'Foraging_True':Foraging_True,
			}
	return render(request, 'sightings/stats.html',context)
