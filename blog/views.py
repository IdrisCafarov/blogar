from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
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
    context = {}

    instructors = Instructor.objects.all()
    context['instructors'] = instructors

    return render(request,"about.html", context)


def contact(request):

    context = {}

    if request.method == 'POST':
        form = ContactForm(request.POST)
        # print(form)
        if form.is_valid():
            form = form.save(commit=False)
            # form.service =
            form.save()
            messages.success(request, 'Sizin müraciətiniz uğurla göndərildi !')
            return redirect(request.META['HTTP_REFERER'])
    else:
        form = ContactForm()

    context['form'] = form


    return render(request, 'contact.html',context)


def search_view(request):

    if request.method == "POST":
        searched = request.POST['searched']
        searched_blogs = Blog.objects.filter(title__contains=searched).order_by('id')
        if searched_blogs:

            context = {
                "searched_blogs":searched_blogs,
                "searched":searched,
            }
            return render(request,"search.html",context)
        else:
            return render(request,"empty_search.html")


def author_detail(request,slug):
    context = {}
    author = get_object_or_404(Instructor,slug=slug)

    context['author'] = author

    return render(request, "author.html", context)