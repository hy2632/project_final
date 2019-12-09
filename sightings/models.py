from django.db import models

# Create your models here.

class Squirrel(models.Model):
	Latitude = models.FloatField()
	Longitude = models.FloatField()
	Unique_Squirrel_ID = models.CharField(max_length=30,primary_key=True)
	Shift_Choices = (
		('AM','AM'),
		('PM','PM'),
	)
	Shift = models.CharField(max_length=2, choices=Shift_Choices)
	Date = models.IntegerField()

	Age_Choices = (
		('', '----'),
		('Adult','Adult'),
		('Juvenile','Juvenile'),
		('?','Unknown')
	)
	Age = models.CharField(max_length=10, choices=Age_Choices, blank=True)


	Primary_Fur_Color = models.CharField(max_length=30, blank=True)
	Location = models.CharField(max_length=30, blank=True)
	Specific_Location = models.CharField(max_length=100, blank=True)

	TF_Choices = (
		# ('', '----'),
		('true','True'),
		('false','False'),
	)
	Running = models.CharField(max_length=10,choices=TF_Choices)
	Chasing = models.CharField(max_length=10,choices=TF_Choices)
	Climbing = models.CharField(max_length=10,choices=TF_Choices)
	Eating = models.CharField(max_length=10,choices=TF_Choices)
	Foraging = models.CharField(max_length=10,choices=TF_Choices)


	Other_Activities = models.CharField(max_length=100, blank=True)
	
	Kuks = models.CharField(max_length=10,choices=TF_Choices)
	Quaas = models.CharField(max_length=10,choices=TF_Choices)
	Moans = models.CharField(max_length=10,choices=TF_Choices)
	Tail_flags = models.CharField(max_length=10,choices=TF_Choices)
	Tail_twitches = models.CharField(max_length=10,choices=TF_Choices)
	Approaches = models.CharField(max_length=10,choices=TF_Choices)
	Indifferent = models.CharField(max_length=10,choices=TF_Choices)
	Runs_from = models.CharField(max_length=10,choices=TF_Choices)
	
	def __str__(self):
		return self.Unique_Squirrel_ID
