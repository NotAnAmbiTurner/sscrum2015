from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext, loader

from .models import User
from .forms import RegisterForm

from .forms import SignUpForm

def index(request):
    register_form = RegisterForm(request.POST or None)	#If we are not posting, this line will do nothing.  It's just an empty form.  That is the purpose of the request.POST parameter
    if register_form.is_valid():
        HttpReturn("Meat Flight!")
        register_form.save()
    return render(request, 'minutes/index.html', locals())


def signup(request):
    title = "Sign Up!"
    form = SignUpForm(request.POST or None)

    context = {
        "title": title,
        "form": form
    }

    if form.is_valid():
        instance = form.save(commit=False)
        full_name = form.cleaned_data.get()

    return render(request, 'minutes/signup.html', context)


def user_page(request):
    # display the user page
    context = {}
    return render(request, 'minutes/user_view.html', context)

def organization_view(request):
    # desplay the organization_view
    context = {}
    return render(request, 'minutes/organization_view.html', context)

def mtgminutes_view(request):
    # display the mtgminutes_view
    context = {}
    return render(request, 'minutes/mtgminutes_view.html',context)

def mtgminutesitem_view(request):
    # display the mtgminutesitem_view
    context ={}
    return render(request, 'minutes/mtgminutesitem_view.html',context)

def hello_world(request):
    context = {}
    return render(request, 'minutes/hello_world.html',context)
