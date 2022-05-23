from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from .models import StartInfo
from .form import updateStartPage
from django.contrib.auth.decorators import login_required

# Create your views here.


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
    return render(request, "update.html",{"form": form})    
    





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
