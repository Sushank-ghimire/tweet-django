# A Basic Tweet CRUD Application With Django Including Authentication Mechanism

## Introduction

This project is a simple **Tweet CRUD (Create, Read, Update, Delete) application** built with Django. It includes an authentication mechanism, allowing users to sign up, log in, create tweets, edit them, and delete their own tweets.

## Features

- **User Authentication** (Signup, Login, Logout)
- **Create Tweets** with content and optional images
- **Read Tweets** (View all tweets and individual tweets)
- **Update Tweets** (Only the tweet owner can edit)
- **Delete Tweets** (Only the tweet owner can delete)
- **Custom 404 Error Page**

---

## Installation and Setup

### Prerequisites

Ensure you have the following installed:

- Python (>= 3.8)
- Django (>= 4.0)
- Virtualenv (Optional but recommended)

### Steps to Setup

#### 1. Clone the repository

```sh
$ git clone https://github.com/Sushank-ghimire/tweet-django.git
$ cd tweet-django
```

#### 2. Create a Virtual Environment (Optional)

```sh
$ python -m venv env
$ source env/bin/activate  # For Linux/macOS
$ env\Scripts\activate    # For Windows
```

#### 3. Install Dependencies

```sh
$ pip install -r requirements.txt
```

#### 4. Apply Migrations & Create Superuser

```sh
$ python manage.py migrate
$ python manage.py createsuperuser
```

#### 5. Run the Server

```sh
$ python manage.py runserver
```

Now open **http://127.0.0.1:8000/** in your browser.

---

## Application Structure

```
tweet-django/
│── megaproject/
│   │── settings.py
│   │── urls.py
│   │── views.py
│── tweet/
│   │── models.py
│   │── views.py
│   │── urls.py
│   │── forms.py
│── templates/
│   │── 404.html
│   │── base.html
│── manage.py
```

---

## Models

### `Tweet` Model (`models.py`)

```python
from django.db import models
from django.contrib.auth.models import User

class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    photo = models.ImageField(upload_to="tweets/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
```

---

## URL Configuration (`urls.py`)

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.tweet_list, name='tweet_list'),
    path('create/', views.tweet_create, name='tweet_create'),
    path('<int:id>/edit/', views.tweet_edit, name='tweet_edit'),
    path('<int:id>/delete/', views.tweet_delete, name='tweet_delete'),
]
```

---

## Views (`views.py`)

### List Tweets

```python
from django.shortcuts import render
from .models import Tweet

def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, 'tweet_list.html', {'tweets': tweets})
```

### Create Tweet

```python
from django.shortcuts import redirect
from .forms import TweetForm

def tweet_create(request):
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForm()
    return render(request, 'tweet_form.html', {'form': form})
```

---

## Custom 404 Page

### `urls.py`

```python
handler404 = "megaproject.views.custom_404_view"
```

### `views.py`

```python
from django.shortcuts import render

def custom_404_view(request, exception):
    return render(request, "404.html", status=404)
```

### `templates/404.html`

```django
{% extends "layout/base.html" %}

{% block title %}404 - Page Not Found{% endblock %}

{% block content %}
<div class="text-center mt-10">
    <h1 class="text-4xl font-bold text-red-600">404 - Page Not Found</h1>
    <p class="mt-2 text-gray-700">Oops! The page you requested does not exist.</p>
    <a href="{% url 'homepage' %}" class="mt-4 px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700">
        Go Back Home
    </a>
</div>
{% endblock %}
```

---

## Authentication Mechanism

- **Signup** (`signup_view`) – Allows users to register
- **Login** (`login_view`) – Authenticates users
- **Logout** (`logout_view`) – Logs users out

### Signup View (`views.py`)

```python
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("tweet_list")
    else:
        form = UserCreationForm()
    return render(request, "signup.html", {"form": form})
```

### Login View

```python
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("tweet_list")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})
```

---

## Conclusion

This project provides a **basic Tweet CRUD functionality** with authentication. You can expand it by:

- Adding **likes/comments**
- Implementing **pagination**
- Enhancing the **UI with Tailwind CSS or Bootstrap**
- Adding **REST API with Django Rest Framework (DRF)**

🚀 **Happy Coding!** 🎉
