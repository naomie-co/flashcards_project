from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User

# Create your models here.

class Package(models.Model):
    name = models.CharField(max_length=200)
    #url = models.URLField(null=True)#add null to try to save the V1 project
    
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
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    number_of_study = models.IntegerField(default=0)
    difficulty = models.CharField(max_length=200)
    date_time = models.DateTimeField(null=True, auto_now_add=True)
    hour = models.TimeField(null=True, blank=True)

    def __str__(self):
        return self.difficulty


class CardForm(ModelForm):
    class Meta:
        model = Card
        #Package field is useless because it was choosen in the previous step
        fields = ['package', 'question', 'answer', 'tag']

        # def save_data(self):
        #     question_check = form.cleaned_data["question"]
        #     answer_check = form.cleaned_data["answer"]
        #     tag_check = form.cleaned_data["tag"]
        #     print(question_check)
        #     new_card = Card.objects.create(
        #         question=question_check,
        #         answer=answer_check,
        #         tag=tag_check)

class PackageForm(ModelForm):
    class Meta:
        model = Package
        fields = ['name']

        # def save_data(self):
        #     name_check = form.cleaned_data["name"]
        #     new_package = Package.objects.create(
        #         name=name_check)