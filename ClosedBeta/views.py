from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponseRedirect
from forms import RegistrationForm


def registrationPage(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username = form.cleaned_data['username'],
                password = form.claned_data['password1'],
                email = form.cleaned_data['email']
            )
            return HttpResponseRedirect('/')
    else:
        form = RegistrationForm()
        return render(request, 'registration/register.html')