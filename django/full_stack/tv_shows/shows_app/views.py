from django.shortcuts import render, redirect
from .models import Show

# Create your views here.
def index(request):
    print('Running index')
    context = {
		"shows": Show.objects.all()
	}
    return render(request, 'index.html', context)

def new(request):
    print('Running new')
    return render(request, 'new.html')

def create(request):
    print('Running create')
    new_show = Show.objects.create(
        title = request.POST['title'],
        network = request.POST['network'],
        release_date = request.POST['release_date'],
        description = request.POST['description']
    )
    return redirect(f'/shows/{new_show.id}')

def show(request, show_id):
    print('Running show')
    context = {
		"show": Show.objects.get(id=show_id)
	}
    return render(request, 'show.html', context)

def edit(request, show_id):
    print('Running edit')
    context = {
		"show": Show.objects.get(id=show_id)
	}
    return render(request, 'edit.html', context)

def update(request, show_id):
    show_to_update = Show.objects.get(id=show_id)
    show_to_update.title = request.POST['title']
    show_to_update.network = request.POST['network']
    show_to_update.release_date = request.POST['release_date']
    show_to_update.description = request.POST['description']
    show_to_update.save()
    return redirect(f'/shows/{show_id}')

def destroy(request, show_id):
    show_to_delete = Show.objects.get(id=show_id)
    show_to_delete.delete()
    return redirect('/shows/')
