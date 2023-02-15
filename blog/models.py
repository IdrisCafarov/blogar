from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from .helper import *


# Create your models here.
class GeneralSettings(models.Model):

    index_top = models.CharField(max_length=300, verbose_name="Top Basliq Index", null=True, blank=True)

    light_logo = models.FileField(verbose_name="light logo(138x35)", blank=True,upload_to="general_settings")
    dark_logo = models.FileField(verbose_name="dark logo(138x35)",null=True ,blank=True,upload_to="general_settings")

    favicon = models.FileField(verbose_name="favicon(100x100)", blank=True, null=True,upload_to="general_settings")



    footer_logo = models.FileField(verbose_name="Footer logo(150x38)",help_text="Saytın aşağısındakı logo", blank=True, null=True,upload_to="general_settings")
    facebook = models.CharField(max_length=1500, verbose_name="Facebook", blank=True)
    linkedin = models.CharField(max_length=1500, verbose_name="Linkedin", blank=True)
    instagram = models.CharField(max_length=1500, verbose_name="Instagram", blank=True)
    twitter = models.CharField(max_length=1500, verbose_name="Twitter", blank=True)

    twitter = models.CharField(max_length=1500, verbose_name="Twitter", null=True, blank=True)



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


class Instructor(models.Model):
    image = models.ImageField(upload_to="Instructors")
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=150)
    about = RichTextField()
    ##Social##
    instagram = models.CharField(max_length=1000, null=True, blank=True)
    facebook = models.CharField(max_length=1000, null=True, blank=True)
    linkedin = models.CharField(max_length=1000, null=True, blank=True)
    twitter = models.CharField(max_length=1000, null=True, blank=True)
    slug = models.SlugField(editable=False, null=True,unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(Instructor, self).save(*args, **kwargs)
        self.slug = seo(self.name + str(self.id))
        super(Instructor, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('author_detail', kwargs={"slug": self.slug})



class Blog(models.Model):
    instructor = models.ForeignKey(Instructor,on_delete=models.CASCADE, related_name="blog", null=True)
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


class Contact(models.Model):
    name = models.CharField(max_length=200)

    email = models.EmailField()
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.email






