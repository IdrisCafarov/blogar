from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Category)

admin.site.register(SubCategory)

@admin.register(Blog)
class AdminBlog(admin.ModelAdmin):
    list_display=['title','click']



admin.site.register(Comment)

