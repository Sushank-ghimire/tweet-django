from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, views
from django.shortcuts import render, redirect

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically logs in after signup
            return redirect('tweets')  # Redirect to the tweet page
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')  # Redirect to homepage or wherever you'd like after login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
# Views of the main app goes here
def index(request):
    return render(request, 'index.html')

def custom_404_view(request, exception):
    return render(request, "404.html", status=404)

def logout(request):
    if request.method == "POST":
        views.auth_logout(request)
        return redirect('homepage')
    return render(request, 'logout.html')