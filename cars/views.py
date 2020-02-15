from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts,Cardetail


# Create your views here.
def index(request):
    return render(request,'newcar.html')


def Post(request,pk):
    sidedata = Posts.objects.all().order_by('-pub_date')[:5]
    postdata = Posts.objects.get(slug=pk)
    relatedata = Posts.objects.filter(slug=pk).values('Category')
    for share in relatedata:
         category =share['Category']
    relateddata = Posts.objects.filter(Category=category)[1:4]
    postdata1 = Posts.objects.filter(slug=pk).values('postviews')
    for share in postdata1:
         viewinc =share['postviews']
    viewinc =viewinc + 1
    print(viewinc)
    postdata.postviews = viewinc
    postdata.save()
    datasplit = Posts.objects.filter(slug=pk).values('desc')
    for share in datasplit:
         viewincs =share['desc']
    dating=viewincs.split('dataslice')

    return render(request,'sharazicarspost.html',{'posttitle':postdata , 'dating':dating ,'sidedata':sidedata ,'relateddata':relateddata})
def Blog(request):
    allposts = Posts.objects.all().order_by('-pub_date')[:10]

    return render(request,'blog-news.html',{'allposts':allposts})
def Brandname(request):
    name =request.GET.get('cars','default')
    cardata = Cardetail.objects.filter(company=name)

    return render(request,'brandname.html',{'cardata':cardata})
def Cardetails(request,pk):
    cardata = Cardetail.objects.get(slug=pk)
    return render(request,'cardetail.html',{'car':cardata})
def Policy(request):
    return render(request,'policy.html')
def About(request):
    return render(request,'about.html')
def Disclaimer(request):
    return render(request,'disclaimer.html')
def Videos(request):
    return render(request,'videos.html')