from django.shortcuts import render
from .models import About

# Create your views here.

def about_detail(request):
    """
    Display About page which can be edited when needed.


    """
    about = About.objects.order_by("title", "content", "updated_on").first()
    if not about:
        return render(request, "about/about.html")
    return render(
        request,
        "about/about.html",
        {
            "post":about
        }
    )