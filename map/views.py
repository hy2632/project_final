from django.shortcuts import render
# Create your views here.
from sightings.models import Squirrel
# from sightings.forms import SquirrelForm #Build a Form

def index(request):
	sightings = Squirrel.objects.order_by('?')[0:99]
	context={'sightings':sightings}
	return render(request, 'map/map.html',context)
