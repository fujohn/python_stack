from django.shortcuts import render, redirect 

def index(request):
    if 'counter' in request.session and 'visited' in request.session:
        request.session['counter'] += 1
        request.session['visited'] += 1
    else:
        request.session['counter'] = 1
        request.session['visited'] = 1
    return render(request, 'count.html')

def destroy(request):
    del request.session['counter']
    del request.session['visited']
    return redirect('/numbers')

def double(request):
    if 'counter' in request.session:
        request.session['counter'] += 1
    return redirect('/numbers')

def add(request):
    if 'counter' in request.session:
        request.session['counter'] += int(request.POST['count']) - 1
    return redirect('/numbers')