from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views
from django.contrib.auth import forms as auth_forms
from accounts.forms import SignUpForm,UserLoginForm
from django.contrib import messages
from django.conf import settings
from django.urls import reverse_lazy
from catalog.models import Reviews,BookInstance,UserHistory
class PasswordChangeView(auth_views.PasswordChangeView):
    form_class=auth_forms.PasswordChangeForm
    success_url=reverse_lazy('profile')
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
            user = authenticate(request,username=username, password=password)
            login(request, user)
            return redirect('index')
   
    return render(request, 'accounts/sign_up.html', {'form': form})
@login_required
def profile(request):
    Logged_in_user_reviews = Reviews.objects.filter(Reviewuser=request.user)
    Logged_in_user_borrowed=BookInstance.objects.filter(BookUser=request.user)
    Past_borrowed_books=UserHistory.objects.filter(BookUser=request.user)
    return render(request, 'accounts/profile.html',{'user_reviews': Logged_in_user_reviews,'User_books':Logged_in_user_borrowed,"User_history":Past_borrowed_books})
def custom_login_view(request):
    form=UserLoginForm(request.POST)
    if request.method=='POST':
        if form.is_valid():
            username =form.cleaned_data.get('username') 
            password = form.cleaned_data.get('password')

            user = authenticate(
                request=request,  # this is the important custom argument
                username=username,
                password=password,
            )

            if user is not None:
                login(request, user)
                return redirect('index')
            elif user is None:
               messages.error(request, 'Failed Login! Invalid Usenrname or Password')
    return render(request,"accounts/login.html", {'form': form})
   
def Lockout(request):
    context = {'cooloff_time': settings.AXES_COOLOFF_TIME}
    newContext={"FAIL",attempt.get_user_attempts(request)}
    return render(request,"accounts/lockout.html",newContext)
# Create your views here.
