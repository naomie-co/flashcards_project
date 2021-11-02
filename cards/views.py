from django.shortcuts import render, redirect, get_object_or_404 
from django.views.generic.edit import FormView
from django.core.paginator import Paginator
from .models import CardForm, PackageForm, Card, Package


# Create your views here.


def index(request):
    """Function to display the home page"""
    packages = Package.objects.order_by('name')

    context = {
        'packages': packages,
        }
    return render(request, 'cards/index.html', context)

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





def learn(request, package):
    """Display and learn a flashcard"""

    get_package = get_object_or_404(Package, name=package)
    paginator = Paginator(get_package, 1)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'cards/learn.html', {'page_obj': page_obj})
