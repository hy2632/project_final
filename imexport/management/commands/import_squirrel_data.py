from django.core.management.base import BaseCommand, CommandError
import urllib.request
import os



class Command(BaseCommand):
	help = 'Import data into DB from csv'

	def add_arguments(self, parser):
	    parser.add_argument('directory', type=str)

	def handle(self, *args, **kwargs):
		from sightings.models import Squirrel
		import csv

		directory = kwargs['directory']
		def read_csv():
		    df = []
		    with open(directory, 'r', newline='', encoding='utf-8') as csvfile:
		        reader = csv.reader(csvfile, delimiter=',')
		        for row in reader:
		            df+=[row]
		    df_new = {}

		    for i in range(len(df)):
		        df_new[i]=df[i][0:3]+df[i][4:6]+df[i][7:9]+df[i][12:13]+df[i][14:29]

		    return df_new



		def save_data(cnt:int):
		    s = Squirrel(
		        Latitude = float(df_new[cnt][1]), 
		        Longitude = float(df_new[cnt][0]), 
		        Unique_Squirrel_ID = df_new[cnt][2],
		        Shift = df_new[cnt][3],
		        Date = int(df_new[cnt][4]),
		        Age =df_new[cnt][5],
		        Primary_Fur_Color =df_new[cnt][6],
		        Location =df_new[cnt][7],
		        Specific_Location =df_new[cnt][8],
		        Running =df_new[cnt][9],
		        Chasing =df_new[cnt][10],
		        Climbing =df_new[cnt][11],
		        Eating =df_new[cnt][12],
		        Foraging =df_new[cnt][13],
		        Other_Activities =df_new[cnt][14],
		        Kuks =df_new[cnt][15],
		        Quaas =df_new[cnt][16],
		        Moans =df_new[cnt][17],
		        Tail_flags =df_new[cnt][18],
		        Tail_twitches =df_new[cnt][19],
		        Approaches =df_new[cnt][20],
		        Indifferent =df_new[cnt][21],
		        Runs_from =df_new[cnt][22],
		)
		    return s
		#     s.save()

		df_new = read_csv()
		for i in range(1,len(df_new)):
		    save_data(i).save()
		    


