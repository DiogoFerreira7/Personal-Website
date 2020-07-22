from django.shortcuts import render

# Create your views here.
def home_view(response):
    return render(response, 'home/home.html', {})