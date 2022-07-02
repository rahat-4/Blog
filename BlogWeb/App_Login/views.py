from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import UserEditProfile, UserSignUp, AddProfilePic



# Create your views here.


# class UserSignUp(CreateView):
#     model = UserCreationForm
#     fields = ('username', 'firstname', 'lastname',
#               'password1', 'password2', 'email')
#     template_name = 'App_Login/user_signup.html'


def user_signup(request):
    form = UserSignUp()
    registered = False

    if request.method == "POST":
        form = UserSignUp(request.POST)

        if form.is_valid():
            form.save()
            registered = True
    dict = {'form': form, 'registered':registered}
    return render(request, 'App_Login/user_signup.html', dict)


def user_login(request):
    form = AuthenticationForm()
    
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        
        if form.is_valid():
            # username = form.cleaned_data.get('username')
            # password = form.cleaned_data.get('password')
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('App_Login:user_profile'))
                else:
                    HttpResponse("Your account already deleted.")
                
    dict = {'form':form}         
    return render(request, 'App_Login/user_login.html', dict)

@login_required
def user_profile(request):
    return render(request, 'App_Login/user_profile.html')

@login_required
def user_edit_profile(request):
    form = UserEditProfile(instance=request.user)
    
    if request.method == "POST":
        form = UserEditProfile(request.POST, instance=request.user)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("App_Login:user_profile"))
    dict={'form':form}
    return render(request, "App_Login/user_edit_profile.html", dict)
    
# class UserEditProfile(UpdateView):
#     model = User
#     fields = ('username','first_name','last_name','email','password')
#     template_name = 'App_Login/user_edit_profile.html'

@login_required
def user_add_img(request):
    form = AddProfilePic()
    
    if request.method == "POST":
        form = AddProfilePic(request.POST, request.FILES)
        if form.is_valid():
            user_obj = form.save(commit=False)
            user_obj.user = request.user
            user_obj.save()    
            return HttpResponseRedirect(reverse('App_Login:user_profile'))
        
    dict={'form':form}
    return render(request,"App_Login/user_add_img.html",dict)

@login_required
def user_change_img(request):
    form = AddProfilePic(instance=request.user.user_profile)
    
    if request.method == "POST":
        form = AddProfilePic(request.POST,request.FILES, instance=request.user.user_profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('App_Login:user_profile'))
        
    dict={'form':form}
    return render(request,"App_Login/user_add_img.html",dict)

@login_required
def user_change_pass(request):
    form = PasswordChangeForm(request.user)
    changed = False
    
    if request.method == "POST":
        form = PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            form.save()
            changed= True
    
    dict = {'form':form, 'changed':changed}
    return render(request, "App_Login/user_change_pass.html", dict)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('App_Login:user_login'))
