from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from accounts.forms import SignUpForm

def signup(request):
    form = SignUpForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            user=form.save()
            user.refresh_from_db()
            user.profile.id_number=form.cleaned_data.get('id_number')
            user.save()
            username=form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            return redirect('index')
    return render(request, 'accounts/sign_up.html', {'form': form})
# Create your views here.
