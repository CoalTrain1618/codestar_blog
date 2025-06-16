from django.shortcuts import render, get_object_or_404
from .models import About

# Create your views here.

def about_detail(request):
    queryset = About.objects.order_by("title", "content", "updated_on")
    post = get_object_or_404(queryset)

    return render(
        request,
        "about/about.html",
        {
            "post":post
        }
    )