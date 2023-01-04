from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Show
import bcrypt

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
    errors = Show.objects.basic_validator(request.POST)
    print(errors)
    if len(errors) > 0:
        for key, value in errors.items():
            print(key, ':', value)
            messages.error(request, value)
        return redirect('/shows/new')
    else:
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
    errors = Show.objects.basic_validator(request.POST)
    print(len(errors))
    if len(errors) > 0:
        for key, value in errors.items():
            print(key, ':', value)
            messages.error(request, value)
        return redirect(f'/shows/{show_id}/edit')
    else:
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

# def validate_login(request):
#     user = User.objects.get(email=request.POST['email'])  # hm...is it really a good idea to use the get method here?
#    if bcrypt.checkpw(request.POST['password'].encode(), user.pw_hash.encode()):
#         print("password match")
#     else:
#         print("failed password")

def register(request):    
    # include some logic to validate user input before adding them to the database!
    password = request.POST['password']
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()  # create the hash    
    print(pw_hash)      # prints something like b'$2b$12$sqjyok5RQccl9S6eFLhEPuaRaJCcH3Esl2RWLm/cimMIEnhnLb7iC'    
    # be sure you set up your database so it can store password hashes this long (60 characters)
    # make sure you put the hashed password in the database, not the one from the form!
    User.objects.create(username=request.POST['username'], password=pw_hash) 
    return redirect("/") # never render on a post, always redirect!    

def login(request):
    # see if the username provided exists in the database
    user = User.objects.filter(username=request.POST['username']) # why are we using filter here instead of get?
    if user: # note that we take advantage of truthiness here: an empty list will return false
        logged_user = user[0]
        # assuming we only have one user with this username, the user would be first in the list we get back
        # of course, we should have some logic to prevent duplicates of usernames when we create users
        # use bcrypt's check_password_hash method, passing the hash from our database and the password from the form
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            # if we get True after checking the password, we may put the user id in session
            request.session['userid'] = logged_user.id
            # never render on a post, always redirect!
            return redirect('/success')
    # if we didn't find anything in the database by searching by username or if the passwords don't match, 
    # redirect back to a safe route
    return redirect("/")
