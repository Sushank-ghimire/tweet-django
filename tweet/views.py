from django.shortcuts import render, redirect
from .models import Tweet
from .forms import TweetForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

# Views of the tweet app
def tweet(request):
    isLoggedin = request.user.is_authenticated
    tweet_collection = Tweet.objects.all().order_by('-created_at')
    return render(request, 'tweet.html', { 'tweets' : tweet_collection, 'isLoggedin': isLoggedin})

@login_required
def create_tweet(request):
    isLoggedin = request.user.is_authenticated
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweets')
    else:
        form = TweetForm()
    return render(request, 'tweet_form.html', { 'form' : form, 'isLoggedin': isLoggedin})

@login_required
def tweet_edit(request, tweet_id):
    isLoggedin = request.user.is_authenticated
    tweet = get_object_or_404(Tweet, pk=tweet_id, user = request.user)
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweets')
    else:
        form = TweetForm(instance=tweet)
    return render(request, 'tweet_form.html', { 'form' : form, 'isLoggedin': isLoggedin})


@login_required
def delete_tweet(request, tweet_id):
    isLoggedin = request.user.is_authenticated
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method == 'POST':
        tweet.delete()
        return redirect('tweets')
    return render(request, 'tweet_delete.html', { 'tweet' : tweet, 'isLoggedin': isLoggedin})