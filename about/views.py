from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import CollaborateForm


# Create your views here.

def about_detail(request):
    """
    Display About page which can be edited when needed.


    """
    if request.method == "POST":
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Collaboration request received! I endeavor to respond within 2 working days'
            )

    about = About.objects.order_by("title", "content", "updated_on").first()
    collaborate_form = CollaborateForm()

    if not about:
        return render(request, "about/about.html")
    return render(
        request,
        "about/about.html",
        {
            "about":about,
            "collaborate_form":collaborate_form
        }
    )



