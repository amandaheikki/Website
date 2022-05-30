from tkinter import E
from django.shortcuts import get_object_or_404, redirect, render, HttpResponseRedirect
from .models import StartModel, EstimateModel, ContactModel, AboutModel, ReferenceImage, ServiceModel
from .form import updateStartPage, updateStartPageContent1, updateStartPageContent2, updateStartPageContent3, updateAboutPage, updateAboutContent1, updateAboutContent2, updateServiceHeading, updateServiceContent1, updateServiceContent2, updateEstimateHeading
from django.contrib.auth.decorators import login_required
from .form import *
from django.contrib import messages

# Create your views here.

# All updates for index/startpage
def startpage_items(request):
    obj=StartModel.objects.all()
    return render(request, "index.html", {"obj":obj})


@login_required
def startpage_update(request, id):
    obj=get_object_or_404(StartModel, id=id)
    if request.method == "POST":
        form=updateStartPage(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form=updateStartPage()
    return render(request, "update.html",{"form":form})    


def startpage_content(request):
    obj=StartModel.objects.all()
    return render(request, "index.html", {"obj":obj})

@login_required
def startpage_contentupd1(request, id):
    obj=get_object_or_404(StartModel, id=id)
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
    obj=get_object_or_404(StartModel, id=id)
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
    obj=get_object_or_404(StartModel, id=id)
    if request.method == "POST":
        form=updateStartPageContent3(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form=updateStartPageContent3()
    return render(request, "updatecontent3.html",{"form":form}) 



# All updates for about us page

def aboutpage_items(request):
    obj=AboutModel.objects.all()
    return render(request, "about.html", {"obj":obj})

@login_required
def aboutpage_update(request, id):
    obj=get_object_or_404(AboutModel, id=id)
    if request.method == "POST":
        form=updateAboutPage(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/about")
    else:
        form=updateAboutPage()
    return render(request, "update_about1.html",{"form":form})    

@login_required
def aboutpage_updateBox1(request, id):
    obj=get_object_or_404(AboutModel, id=id)
    if request.method == "POST":
        form=updateAboutContent1(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/about")
    else:
        form=updateAboutContent1()
    return render(request, "update_about2.html",{"form":form})   

@login_required
def aboutpage_updateBox2(request, id):
    obj=get_object_or_404(AboutModel, id=id)
    if request.method == "POST":
        form=updateAboutContent2(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/about")
    else:
        form=updateAboutContent2()
    return render(request, "update_about3.html",{"form":form})  

# SERVICE

def services_items(request):
    obj=ServiceModel.objects.all()
    return render(request, "services.html", {"obj":obj})

@login_required
def update_servicesheading(request, id):
    obj=get_object_or_404(ServiceModel, id=id)
    if request.method == "POST":
        form=updateServiceHeading(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/services")
    else:
        form=updateServiceHeading()
    return render(request, "update_serviceheading.html",{"form":form})  

@login_required
def update_servicescontent1(request, id):
    obj=get_object_or_404(ServiceModel, id=id)
    if request.method == "POST":
        form=updateServiceContent1(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/services")
    else:
        form=updateServiceContent1()
    return render(request, "update_service1.html",{"form":form})  

@login_required
def update_servicescontent2(request, id):
    obj=get_object_or_404(ServiceModel, id=id)
    if request.method == "POST":
        form=updateServiceContent2 (request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/services")
    else:
        form=updateServiceContent2()
    return render(request, "update_service2.html",{"form":form})  



#ESTIMATE
def estimate_items(request):
    obj=EstimateModel.objects.all()
    return render(request, "estimate.html", {"obj":obj})

@login_required
def update_estimateheading(request, id):
    obj=get_object_or_404(ServiceModel, id=id)
    if request.method == "POST":
        form=updateEstimateHeading(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/estimate")
    else:
        form=updateServiceHeading()
    return render(request, "update_estimateheading.html",{"form":form})  

#CONTACT
def contact_items(request):
    obj=ContactModel.objects.all()
    return render(request, "contact.html", {"obj":obj})

@login_required
def update_contactheading(request, id):
    obj=get_object_or_404(ServiceModel, id=id)
    if request.method == "POST":
        form=updateContactHeading(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/contact")
    else:
        form=updateContactHeading()
    return render(request, "update_contactheading.html",{"form":form})  



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
