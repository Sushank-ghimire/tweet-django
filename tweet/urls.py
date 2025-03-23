from django.urls import path
from . import views

# Tweet app routes
urlpatterns = [
    path('', views.tweet, name="tweet"),
]
