from django.shortcuts import render
from .models import Posts

# Create your views here.
def index(request):
    return render(request, "feed/index.html", {'posts': Posts.objects.all()[:5]})
