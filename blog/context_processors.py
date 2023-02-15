from blog.models import *

def extras(request):
    context = {}
    settings = GeneralSettings.objects.all()
    context['settings'] = settings

    return context