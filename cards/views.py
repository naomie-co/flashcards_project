from django.shortcuts import render

# Create your views here.



def index(request):
    """Function to display the home page"""
    return render(request, 'cards/index.html')


def create(request):
    """Function to display the flashcard creation page"""
    return render(request, 'cards/create.html')

