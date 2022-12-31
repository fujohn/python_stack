from django.shortcuts import render, HttpResponse, redirect
# other imports
from .models import Movie

# show all of the data from a table
def index(request):
    context = {
        "all_the_movies": Movie.objects.all()
    }
    return render(request, "index.html", context)

def index_2(request): # for one to many
    context = {"authors": Author.objects.all()}		# we're only sending up all the authors
    return render(request, "index.html", context)

