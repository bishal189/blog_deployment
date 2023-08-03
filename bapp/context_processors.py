
from .models import Category
from assignment.models import socail_platforms
def get_category(request):
    category=Category.objects.all()
    return dict(category=category)



def get_platforms(request):
    platform=socail_platforms.objects.all()
    return dict(platform=platform)
