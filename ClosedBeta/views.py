from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponseRedirect
from forms import RegistrationForm
from Article.models import Article

def index(request):
    articles = Article.objects.all()[:10]
    return render(request, "ClosedBeta/index.html", {"articles": articles})

def registrationPage(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password1'],
                email = form.cleaned_data['email']
            )
            return HttpResponseRedirect('/')
        return render( request, 'registration/register.html', {"form": form,} )
    else:
        form = RegistrationForm()
        return render( request, 'registration/register.html', {"form": form,} )