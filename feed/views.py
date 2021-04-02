from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Posts
from .forms import NameForm

# Create your views here.
def index(request):
    return render(request, "feed/index.html", {'posts': Posts.objects.all()[:5]})

def post_something(request):
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['usern']

            return HttpResponseRedirect('/feed/')

    else:
        form = NameForm()
    return render(request, 'feed/post_something.html', {'form': form})
