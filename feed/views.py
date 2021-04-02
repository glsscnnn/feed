from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Posts
from .forms import NameForm

# Create your views here.
def index(request):
    return render(request, "feed/index.html", {'posts': reversed(Posts.objects.order_by('-date'))})

def post_something(request):
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            values = form.save(commit=False)
            values.save()
            return HttpResponseRedirect('/')

    else:
        form = NameForm()
    return render(request, 'feed/post_something.html', {'form': form})
