from django.shortcuts import render
from .models import Contact,Cources
from datetime import *
# Create your views here.
what_want_learn=[]


def index(request):  
    recomend=[]
    for item in Cources.objects.all():
        print(item.reco)
        if(item.reco):
            recomend.append(item)
    context={"ct_class":recomend}
    return render(request,'index.html',context)

def contact(request):
    if request.method == "POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        dohelp=request.POST.get("helpbox")
        scon=Contact(name=name,email=email,desc=dohelp,date=datetime.now())
        scon.save()
    return render(request,'contact.html')

def courcesP(request):
    courcn=[]
    for item in Cources.objects.all():
         courcn.append(item)
    context={"ct_class":courcn}
    return render(request,'cources.html',context)


def learn(request,slug):
    post=Cources.objects.get(slug=slug)
    context={"cdata":post}
    return render(request,'learn.html',context)


def search(request):
    search_post = request.GET.get('search')
    found=[]
    h_founds=0
    for item in Cources.objects.all():
         if search_post != "":
            if item.title == search_post:
                found.append(item)
                h_founds+=1
            elif search_post in item.title:
                found.append(item)
                h_founds+=1
            elif item.title == search_post.lower():
                found.append(item)
                h_founds+=1
            elif item.title == search_post.upper():
                found.append(item)
                h_founds+=1
            elif search_post.lower() in item.title:
                found.append(item)
                h_founds+=1
            elif search_post.upper() in item.title:
                found.append(item)
                h_founds+=1
         else:
             search_post="none"
    context={"ct_class":found,"fresult":h_founds,"sched":search_post}
    return render(request,'search.html',context)


def aboutus(request):
    return render(request,'about.html')
        