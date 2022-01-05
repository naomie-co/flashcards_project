from django.shortcuts import render, redirect, get_object_or_404 
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import CardForm, PackageForm, Card, Package
from django.http import HttpResponse #testCookies
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
        id_package = Package.objects.get(name=package)
        get_cards = Card.objects.filter(package=id_package.id)

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
        now = datetime.datetime.now()
        print(now)
        form = Form(request.POST)
        answer_data = form.cleaned_data["card"]
        answer_status = form.cleaned_data["status"]
        print(answer_date, answer_status, now)
    return HttpResponse("réponse enregistrée!")

    # if request.method == 'POST':
    #     if request.session.test_cookie_worked():
    #         request.session.delete_test_cookie()
    #         return HttpResponse("You're logged in.")
    #     else:
    #         return HttpResponse("Please enable cookies and try again.")
    # request.session.set_test_cookie()
    # return render(request, 'foo/login_form.html')




# def login(request):
#     """Function to display the login page"""
    
#     return render(request, 'cards/login.html', context)


# def logout_view(request):
#     logout(request)
#     return render(request, 'cards/index.html') 