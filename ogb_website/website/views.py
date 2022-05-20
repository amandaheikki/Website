from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html', {})

def references(request):
    return render(request, 'references.html', {})

def contact(request):
    return render(request, 'contact.html', {})

def faq(request):
    return render(request, 'faq.html', {})
