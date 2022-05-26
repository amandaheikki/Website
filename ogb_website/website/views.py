from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from .models import FooterAbout, StartInfo
from .form import updateStartPage, updateFooter
from django.contrib.auth.decorators import login_required

# Create your views here.

# All updates for index/startpage
def startpage_items(request):
    obj=StartInfo.objects.all()
    return render(request, "index.html", {"obj":obj})


@login_required
def startpage_update(request, id):
    obj=get_object_or_404(StartInfo, id=id)
    if request.method == "POST":
        form=updateStartPage(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form=updateStartPage()
    return render(request, "update.html",{"form":form})    
    
#Update footer info
def footer_item(request):
    footerobj=FooterAbout.objects.all()
    return render(request, "footer.html", {"footerobj":footerobj})

@login_required
def footer_update(request, id):
    footerobj=get_object_or_404(FooterAbout, id=id)
    if request.method == "POST":
        form=updateFooter(request.POST, instance=footerobj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form=updateFooter()
    return render(request, "update_footer.html", {"form":form})  

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
