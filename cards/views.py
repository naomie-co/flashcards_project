from django.shortcuts import render
from django.views.generic.edit import FormView
from .models import CardForm, PackageForm, Card, Package


# Create your views here.


def index(request):
    """Function to display the home page"""
    return render(request, 'cards/index.html')


def package(request):
    """Function to create or select a package before creating cards"""
    
    if request.method == "POST":
        form = PackageForm(request.POST)
        if form.is_valid():
            name_check = form.cleaned_data["name"]
            new_package = Package.objects.create(
                name=name_check)

        #data = {
        #"package_name" : name_check,
        #}
        #form = CardForm(data)
        form = CardForm()
        
        #form.fields['package'] = name_check

        context = {
        'form': form,
        'package_name': name_check,
        }
        
        return render(request, 'cards/create.html', context)

    else:
        form = PackageForm()
        context = {
        'form': form,
        }

        return render(request, 'cards/package.html', context)

def create(request, package):
    """Function to create a flashcard"""

    #error = False

    if request.method == "POST":
        print("Welcome to the POST!")
        form = CardForm(request.POST)
        if form.is_valid():
            question_check = form.cleaned_data["question"]
            answer_check = form.cleaned_data["answer"]
            package_name = package
            tag_check = form.cleaned_data["tag"]
            print(question_check)
            new_card = Card.objects.create(
                question=question_check,
                answer=answer_check,
                package=package_name, 
                tag=tag_check)
        form = CardForm()

        context = {
        'form': form,
        'package_name': package,
        }


    else:
        form = CardForm()

        context = {
        'form': form,
        }

    return render(request, 'cards/create.html', context)
"""
 error = False

    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
            else: # error message
                error = True
    else:
        form = ConnexionForm()

    return render(request, 'account/log_in.html', locals())
      

        try:
            product = request.POST.get('product')
            user = request.POST.get('user')
            prod = op_food.objects.get(id=product)
            user_id = User.objects.get(id=user)
            substitute.objects.get_or_create(id_substitute=prod, user=user_id)
        except IntegrityError:
            error = True

            """