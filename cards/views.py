from django.shortcuts import render, redirect, get_object_or_404 
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import CardForm, Card, Package, Learning_statistics, Package
from django.http import HttpResponse #testCookies
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import datetime
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
        #print("Dans Create/get")

    context = {
        'form': form,
#            'package': package_name,
        }
    return render(request, 'cards/create.html', context)
        #return redirect('create', package=package_name)





def learn(request, package):
    """Display and learn a flashcard"""
    
    if request.method == "GET":
        find_package = get_object_or_404(Package, name=package)
        get_cards = Card.objects.filter(package=find_package.id)

        #Display cards with pagination
        paginator = Paginator(get_cards, 1)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        try:
            cards = paginator.page(page_number)
        except PageNotAnInteger:
            cards = paginator.page(1)
        except EmptyPage:
            cards = paginator.page(paginator.num_pages)

        return render(request, 'cards/learn.html', {'page_obj': page_obj, 'cards': cards})

    # else: 
    #     if request.method == "POST":
    #         form = CardForm(request.POST)
    #         if form.is_valid():
    #             answer_data = form.cleaned_data["card"]
    #             answer_status = form.cleaned_data["status"]
        



def learning_stat(request):

    if request.method == "POST":
        # form = CardForm(request.POST)
        # if form.is_valid():
        form = request.POST
        print(form)
        if request.user.is_authenticated:
            user = form.get('user')
            user_id = get_object_or_404(User, id=user)
            card_id = form.get("card")
            card_id = Card.objects.get(id=card_id)
            answer_status = form.get("status")
            date_and_time = datetime.datetime.now() 
            Learning_statistics.objects.create(
                card=card_id, 
                user=user_id, 
                difficulty=answer_status, 
                date_time=date_and_time.strftime("%c"))
            print(user_id, card_id, answer_status, date_and_time)
    #Going back to previous url
    return redirect(request.META['HTTP_REFERER'])
    
    #return HttpResponse("réponse enregistrée!")

def history(request, user):
    if request.user.is_authenticated:
        user_id = user_id = get_object_or_404(User, id=user)
        history = Learning_statistics.objects.filter(user=user_id)
        context = {
            'cards': history,
        }
        return render(request, 'cards/history.html', context)
    else:
        return redirect('accounts:login')
