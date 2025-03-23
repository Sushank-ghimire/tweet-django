from django.shortcuts import render, redirect
from .models import Tweet
from .forms import TweetForm
from django.shortcuts import get_object_or_404

# Views of the tweet app
def tweet(request):
    tweet_collection = Tweet.objects.all().order_by('-created_at')
    print("Tweet collections : ", tweet_collection)
    return render(request, 'index.html', { 'tweets' : tweet_collection})

def create_tweet(request):
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            redirect('tweets')
    else:
        form = TweetForm()
    return render(request, 'tweet_form.html', { 'form' : form})

def tweet_edit(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user = request.user)
    if req.method == "POST":
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            redirect('tweets')
    else:
        form = TweetForm(instance=tweet)
    return render(request, 'tweet_form.html', { 'form' : form})

def delete_tweet(requset, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if requset.method == 'POST':
        tweet.delete()
        return redirect('tweets')
    return render(request, 'tweet_delete.html', { 'tweet' : tweet})