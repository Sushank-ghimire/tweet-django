from django.urls import path
from . import views

# Tweet app routes
urlpatterns = [
    path('', views.tweet, name="tweet"),
    path('create/', views.create_tweet, name="create_tweet")
]
