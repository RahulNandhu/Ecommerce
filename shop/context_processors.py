from .models import Items

def menulinks(request):
    links=Items.objects.all()
    return {'links':links}
