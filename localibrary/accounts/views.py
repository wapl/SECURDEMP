from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from accounts.forms import SignUpForm

def signup(request):
    form = SignUpForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    return render(request, 'accounts/sign_up.html', {'form': form})
# Create your views here.
