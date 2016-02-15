from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from book.models import Book

#from forms import MyNewForm
from forms2 import UserForm

def home(request): 
    language = 'en-us'    
    session_language = 'en-us'
    
    if 'lang' in request.COOKIES:
        language = request.COOKIES['lang']
    
    if 'lang' in request.session:
        session_language = request.session['lang']
        
    args = {}
    args.update(csrf(request))
    
    args['books'] = Book.objects.all()
    args['language'] = language
    args['session_language'] = session_language
        
    return render_to_response('home.html', args)


def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login.html', c)

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/loggedin')
    
    else:
        return HttpResponseRedirect('/invalid')
    
def loggedin(request):
    return render_to_response('loggedin.html',
                              {'full_name': request.user.username})
    
def invalid_login(request):
    return render_to_response('invalid_login.html')
    
def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')    

def register_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        #form = MyNewForm(request.POST)
      
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/sign_up_success')
        
    args = {}
    args.update(csrf(request))
        
    #args['form'] = MyNewForm()
    args['form'] = UserForm()
    
        
    return render_to_response('register.html', args)

def register_success(request):
    return render_to_response('register_success.html')

def about(request):
    return render_to_response('about.html')

def contact(request):
    return render_to_response('contact.html')
