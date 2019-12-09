from django.core.management.base import BaseCommand, CommandError
import urllib.request
import os
from sightings.models import Squirrel
import pandas as pd



class Command(BaseCommand):
	help = 'Export data from DB into csv'

	def add_arguments(self, parser):
	    parser.add_argument('directory', type=str)

	def handle(self, *args, **kwargs):
		directory = kwargs['directory']
		list_sqr = list(Squirrel.objects.all().values())
		df = pd.DataFrame(list_sqr)
		df.to_csv(directory)

