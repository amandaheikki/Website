from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from .models import StartPage
from .form import updateStartPage, updateStartPageContent1, updateStartPageContent2, updateStartPageContent3
from django.contrib.auth.decorators import login_required
from .form import *

# Create your views here.

# All updates for index/startpage
def startpage_items(request):
    obj=StartPage.objects.all()
    return render(request, "index.html", {"obj":obj})


@login_required
def startpage_update(request, id):
    obj=get_object_or_404(StartPage, id=id)
    if request.method == "POST":
        form=updateStartPage(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form=updateStartPage()
    return render(request, "update.html",{"form":form})    


def startpage_content(request):
    obj=StartPage.objects.all()
    return render(request, "index.html", {"obj":obj})

@login_required
def startpage_contentupd1(request, id):
    obj=get_object_or_404(StartPage, id=id)
    if request.method == "POST":
        form=updateStartPageContent1(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form=updateStartPageContent1()
    return render(request, "updatecontent.html",{"form":form})  

@login_required
def startpage_contentupd2(request, id):
    obj=get_object_or_404(StartPage, id=id)
    if request.method == "POST":
        form=updateStartPageContent2(request.POST,request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form=updateStartPageContent2()
    return render(request, "updatecontent2.html",{"form":form})  

@login_required
def startpage_contentupd3(request, id):
    obj=get_object_or_404(StartPage, id=id)
    if request.method == "POST":
        form=updateStartPageContent3(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form=updateStartPageContent3()
    return render(request, "updatecontent3.html",{"form":form}) 


#def index(request):
 #   return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html', {})

def references(request):
    return render(request, 'references.html', {})

def contact(request):
    return render(request, 'contact.html', {})

def faq(request):
    return render(request, 'faq.html', {})

def services(request):
    return render(request, 'services.html', {})    

def estimate(request):
    return render(request, 'estimate.html', {})    
