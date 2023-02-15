from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Category)

admin.site.register(SubCategory)

@admin.register(Blog)
class AdminBlog(admin.ModelAdmin):
    list_display=['title','click']



admin.site.register(Comment)

admin.site.register(Contact)

admin.site.register(Instructor)


MAX_OBJECTS = 1

@admin.register(GeneralSettings)
class AdminGeneralSettings(admin.ModelAdmin):

    def has_add_permission(self, request):
          if self.model.objects.count() >= MAX_OBJECTS:
               return False
          return super().has_add_permission(request)
