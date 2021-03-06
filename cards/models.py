from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User


class Package(models.Model):
    name = models.CharField(max_length=200)
    #url = models.URLField(null=True)
    
    def __str__(self):
        return self.name




class Card(models.Model):
    question = models.CharField(max_length=2000)
    answer = models.CharField(max_length=2000)
    package = models.ForeignKey(Package, on_delete=models.CASCADE, null=True)
    tag = models.CharField(max_length=200)

    def __int__(self):
        return self.id


class Learning_statistics(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    difficulty = models.CharField(max_length=200)
    date_time = models.DateTimeField(null=True, auto_now_add=True)

    def __str__(self):
        return self.difficulty


class CardForm(ModelForm):
    class Meta:
        model = Card
        fields = ['package', 'question', 'answer', 'tag']

"""    
class PackageForm(ModelForm):
    class Meta:
        model = Package
        fields = ['name']
"""