from .models import Category

def categories_links(request):
    categories = Category.objects.all()
    return dict(categories=categories)