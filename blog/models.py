from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from .helper import *


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="categories")
    slug = models.SlugField(editable=False, null=True,unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Categories"



    def save(self, *args, **kwargs):
        super(Category, self).save(*args, **kwargs)
        self.slug = seo(self.title)
        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={"slug": self.slug})
    


class SubCategory(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="sub_categories")
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="sub")
    pin = models.BooleanField(default=False)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name_plural = "Sub Categories"




class Blog(models.Model):
    title = models.CharField(max_length=200)
    main_image = models.ImageField(upload_to="blogs",null=True)
    slider_image = models.ImageField(upload_to="blogs",null=True)


    image_1 = models.ImageField(upload_to="blogs",null=True,blank=True)
    text_1 = RichTextField(null=True,blank=True)

    image_2 = models.ImageField(upload_to="blogs",null=True,blank=True)
    text_2 = RichTextField(null=True,blank=True)

    image_3 = models.ImageField(upload_to="blogs",null=True,blank=True)
    text_3 = RichTextField(null=True,blank=True)


    created_date = models.DateField(auto_now_add=True)
    click = models.IntegerField(default=0,editable=False,null=True)
    sub = models.ForeignKey(SubCategory,on_delete=models.CASCADE,related_name="blogs",null=True)
    slug = models.SlugField(editable=False, null=True,unique=True)



    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):
        super(Blog, self).save(*args, **kwargs)
        self.slug = seo(self.title)
        super(Blog, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={"slug": self.slug})

        
class Comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    comment = models.TextField()
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE,related_name="comments")
    created_date = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.email

    
    

    
