from django.shortcuts import render

def index(request):
    return render(request, 'aboutme/index.html')

def contacts(request):
    return render(request, 'aboutme/contacts.html')

def aboutme(request):
    return render(request, 'aboutme/aboutme.html')