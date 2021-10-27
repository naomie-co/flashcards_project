from django.shortcuts import render, redirect 
from django.views.generic.edit import FormView
from .models import CardForm, PackageForm, Card, Package


# Create your views here.


def index(request):
    """Function to display the home page"""
    return render(request, 'cards/index.html')

"""
def package(request):
    #Function to create or select a package before creating cards
    
    if request.method == "POST":
        form = PackageForm(request.POST)
        if form.is_valid():
            package_name = form.cleaned_data["name"]
            print("Le nom du paquet est: ", package_name)
            new_package = Package.objects.create(
                name=package_name)

        return redirect('create', package=package_name)

    else:
        form = PackageForm()
        context = {
        'form': form,
        }

        return render(request, 'cards/package.html', context)
"""

def create(request):
    """Function to create a flashcard"""

    #error = False
    if request.method == "POST":
        form = CardForm(request.POST)
        if form.is_valid():
            question_check = form.cleaned_data["question"]
            answer_check = form.cleaned_data["answer"]
            package_name = form.cleaned_data["package"]
            tag_check = form.cleaned_data["tag"]
            print(question_check)
            new_card = Card.objects.get_or_create(
                question=question_check,
                answer=answer_check,
                package=package_name, 
                tag=tag_check)
        form = CardForm()
        #return redirect('create', package=package_name)


    else:
        form = CardForm()
        print("Dans Create/get")

    context = {
        'form': form,
#            'package': package_name,
        }
    return render(request, 'cards/create.html', context)
        #return redirect('create', package=package_name)





def learn(request):
    """Display and learn a flashcard"""

    #display the packages available (get)
    #when the user choose a package, send back the cards (print step by step)

    return render(request, 'cards/learn.html', context)