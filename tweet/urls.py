from django.urls import path
from . import views

# Tweet app routes
urlpatterns = [
    path('', views.tweet, name="tweets"),  # Home or main tweet feed view
    path('create/', views.create_tweet, name="create_tweet"),  # URL for creating a tweet
    path('form/', views.create_tweet, name="tweet_form"),  # URL for the tweet creation form (same view as create_tweet)
    path('<int:tweet_id>/delete/', views.delete_tweet, name="tweet_delete"),  # URL for deleting a tweet
    path('<int:tweet_id>/edit/', views.tweet_edit, name="tweet_edit")  # URL for editing a tweet
]
