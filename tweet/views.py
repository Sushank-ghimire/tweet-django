from django.shortcuts import render

# Views of the tweet app
def tweet(request):
    return render(request, 'tweet.html')