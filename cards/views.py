"""Cards views"""
import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from .models import CardForm, Card, Package, Learning_statistics


def index(request):
    """Function to display the home page"""
    packages = Package.objects.order_by('name')

    context = {
        'packages': packages,
        }
    return render(request, 'cards/index.html', context)


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
            Card.objects.get_or_create(
                question=question_check,
                answer=answer_check,
                package=package_name,
                tag=tag_check)
        form = CardForm()
    else:
        form = CardForm()

    context = {
        'form': form,
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


def learning_stat(request):
    """Saved learning data in Learning_statistics table"""
    if request.method == "POST":
        form = request.POST
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
            #print(user_id, card_id, answer_status, date_and_time)
    #Going back to previous url
    return redirect(request.META['HTTP_REFERER'])


def history(request, user):
    """Allows user to see his learning history"""
    if request.user.is_authenticated:
        user_id = user_id = get_object_or_404(User, id=user)
        history = Learning_statistics.objects.filter(user=user_id)
        context = {
            'cards': history,
        }
        return render(request, 'cards/history.html', context)
    else:
        return redirect('accounts:login')
