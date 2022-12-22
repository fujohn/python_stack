from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    # return HttpResponse("this is the equivalent of @app.route('/')!")
    context = {
        "name": "Noelle",
        "favorite_color": "turquoise",
        "pets": ["Bruce", "Fitz", "Georgie"]
    }
    return render(request, "index.html", context)

def create_user(request):
    print("Got Post Info....................")
    name_from_form = request.POST['name']
    email_from_form = request.POST['email']
    context = {
        "name_on_template" : name_from_form,
        "email_on_template" : email_from_form
    }
    return redirect("/success")

def success(request):
    return render(request,"show.html")