from django.shortcuts import render

# Views of the main app goes here
def index(request):
    return render(request, 'index.html')