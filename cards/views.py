from django.shortcuts import render
from .models import CardForm, Card

# Create your views here.







def index(request):
    """Function to display the home page"""
    return render(request, 'cards/index.html')


def create(request):
    """Function to display the flashcard creation page"""

    error = False

    if request.method == "POST":
        form = CardForm(request.POST)
        if form.is_valid():
            question_check = form.cleaned_data["question"]
            answer_check = form.cleaned_data["answer"]
            package_check = form.cleaned_data["package"]
            tag_check = form.cleaned_data["tag"]
            new_card = Card.objects.create(question=question_check, answer=answer_check,\
            package=package_check, tag=tag_check)

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