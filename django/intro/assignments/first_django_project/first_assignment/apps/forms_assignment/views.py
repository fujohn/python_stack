from django.shortcuts import render, redirect 

# Create your views here.
name = None
loc = None
lang = None
com = None


def form(request):
    return render(request, 'form.html')

def save_survey(request):
    print('This is form dict -------------------------')
    request.session['name'] = request.POST["name"]
    request.session['dojo'] = request.POST["dojo"]
    request.session['language'] = request.POST["language"]
    request.session['comment'] = request.POST["comment"]
    return redirect('/forms/result')

def result(request):
    return render(request, 'result.html')