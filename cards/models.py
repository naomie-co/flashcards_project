from django.db import models
from django.forms import ModelForm

# Create your models here.

class Package(models.Model):
	name = models.CharField(max_length=200)
	url = models.URLField(null=True)#add null to try save the first project
	
	def __str__(self):
		return self.name


class Card(models.Model):
	question = models.CharField(max_length=2000)
	answer = models.CharField(max_length=2000)
	package = models.ForeignKey(Package, on_delete=models.CASCADE, null=True)
	tag = models.CharField(max_length=200)

	def __str__(self):
		return self.question


class Learning_history(models.Model):
	card = models.ForeignKey(Card, on_delete=models.CASCADE) 
	number_of_study = models.IntegerField(default=0)
	difficulty = models.CharField(max_length=200)
	date_time = models.DateTimeField(null=True, auto_now_add=True)

	def __str__(self):
		return self.difficulty


class CardForm(ModelForm):
	class Meta:
		model = Card
		fields = ['question', 'answer', 'package', 'tag']