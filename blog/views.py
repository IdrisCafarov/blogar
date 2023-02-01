from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.contrib import messages
from django.utils import timezone
from .models import *
from .forms import *


# Create your views here.

def index(request):
    context = {}

    latests = Blog.objects.order_by('-created_date')
    context['latests'] = latests

    popular_cat = Category.objects.all()
    context['popular_cat'] = popular_cat

    daily_subs = SubCategory.objects.filter(pin=True)
    context["daily_subs"] = daily_subs

    popular_blogs = Blog.objects.order_by("-click")
    context["popular_blogs"] = popular_blogs



    return render(request,"index.html",context)



def category_detail(request,slug):
    context={}

    category = get_object_or_404(Category,slug=slug)
    context["category"] = category

    return render(request,"category_detail.html",context)



def blog_detail(request,slug):
    context = {}
    blog = get_object_or_404(Blog,slug=slug)
    blog.click +=1
    blog.save()
    context["blog"] = blog

    popular_blogs = Blog.objects.all()
    context["popular_blogs"] = popular_blogs


    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.blog=blog
            data.save()
            messages.success(request, 'Sizin kommentiniz uğurla əlavə olundu!')
            return HttpResponseRedirect('#')
    else:
        form = CommentForm()

    context['form'] = form

    return render(request,"detail.html",context)


def handler404(request, exception):
    return render(request, "404.html", {})


def about(request):
     return render(request,"about.html")


def contact(request):

    context = {}
    if request.method == 'POST':

        form = ContactForm(request.POST)
        if form.is_valid():
            message = form.save(commit = False)
            message.created_date = timezone.now
            message.save()
        
            return HttpResponseRedirect('/')
    else:
        form = ContactForm()

    context["form"] = form

    return render(request, 'contact.html',context)


def search_view(request):

    context = {}

    if request.method=='POST':
        searched = request.POST['q']
        blogs=Blog.objects.filter(title__contains=searched)
        return render(request, 'search.html', {'searched':searched, 'blogs':blogs})
    
    else:
        return render(request, 'search.html', {}, context)