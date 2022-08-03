from django.shortcuts import render
from array import array
from urllib import request
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Rentalsapp
from .models import screenbooks
from datetime import date
from datetime import datetime
from django.db.models import Q

# Create your views here.

#This code displays the login form.
def login(request):
    #form = Rentalsapp.objects.all().values()
    template = loader.get_template('login.html')
    #context = {
        #'form': form,
    #}
    #return HttpResponse(template.render(context, request))  
    return HttpResponse(template.render({}, request))

#This code ensures the email and password are valid.
def loginlog(request):
    email = request.POST.get('login__email')
    y = request.POST.get('login__pass')
    error ="";
    

    try:
        mymembers = Rentalsapp.objects.all().values().order_by('lastname')
        print(mymembers)
        print(email)
        print(y)
        match = Rentalsapp.objects.get(email=email,password=y)
        print("here")
        print(match)
        request.session['member_id'] = match.id
        request.session['username'] = match.firstname

        """
        if request.method == 'POST':
            if request.session.test_cookie_worked():
                request.session.delete_test_cookie()
                return HttpResponse("You're logged in.")
            else:
                return HttpResponse("Please enable cookies and try again.")
        request.session.set_test_cookie()
        return render(request, 'foo/login.html')
        """

    except Rentalsapp.DoesNotExist:
        template = loader.get_template('login.html')
        context = {
            'error': "Invalid username or password.",
        }
        return HttpResponse(template.render(context, request))    
    return HttpResponseRedirect(reverse('index'))

#This code displays the record of members in the database.
def indexx(request):
    mymembers = Rentalsapp.objects.all().values().order_by('lastname')

    if request.POST:
        sort = str(request.POST['sort'])
        search = str(request.POST['search']).lower()
        #print(search)
        if search != '':
            mymembers = Rentalsapp.objects.all().values().filter(firstname__contains=search) | Rentalsapp.objects.all().values().filter(lastname__contains=search) | Rentalsapp.objects.all().values().filter(email__contains=search)
            #return HttpResponseRedirect(reverse('index'))
        elif sort == 'firstname':
            mymembers = Rentalsapp.objects.all().values().order_by('firstname')
        elif sort == 'lastname':
            mymembers = Rentalsapp.objects.all().values().order_by('lastname')
        elif sort == 'email':
            mymembers = Rentalsapp.objects.all().values().order_by('email')
        else:
            mymembers = mymembers
            #return HttpResponseRedirect(reverse('index'))

    
    #print(mymembers)  
    reQ = request.session.get('username')      
    template = loader.get_template('indexx.html')
    context = {
        'mymembers': mymembers,
        'username': request.session.get('username'),
        #'sort': sort,
    }
    if reQ == None:
        return HttpResponseRedirect(reverse('login'))
    else:
        return HttpResponse(template.render(context, request))

#This code displays the registration form page.
def register(request):
    template = loader.get_template('registration.html')
    context = {
        'error': '',
    }
    return HttpResponse(template.render(context, request))

#This code ensures the password and confirm password are the same in the registration page, it also ensures the inputed email hasn't been used before.
def addrecord(request):
    if request.POST:
        x = str(request.POST['first__name']).lower()
        y = str(request.POST['last__name']).lower()
        a = str(request.POST['registration__email']).lower()
        c = str(request.POST['regi__pass']).lower()
        d = str(request.POST['pass__con']).lower()
#...ensures password and comfirm password match...
        if c != d:
            template = loader.get_template('registration.html')
            context = {
                'error': 'Password does not match',
            }
            return HttpResponse(template.render(context, request))
        elif "@proxynetgroup" in a:
            #...ensures inputed email hasn't been used before...
            try:
                match = Rentalsapp.objects.get(email=a)

                template = loader.get_template('registration.html')
                context = {
                    'error': "This email has been used. Try another one.",
                }
                return HttpResponse(template.render(context, request))

            except Rentalsapp.DoesNotExist:
                member = Rentalsapp(firstname=x, lastname=y, email=a, password=c,)
                member.save()
                print(member)
            return HttpResponseRedirect(reverse('login'))
        else:
            template = loader.get_template('registration.html')
            context = {
                'error': 'Email must contain @proxynetgroup.com',
            }
            return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect(reverse('index'))

def index(request):
    screens = screenbooks.objects.all().values()
    print(screens)
    reQ = request.session.get('username').upper()
    print(reQ)
    template = loader.get_template('index.html')
    context = {
        'screens':screens,
        'reQ':reQ,
        'username': request.session.get('username')
    }
    
    if reQ == None:
        return HttpResponseRedirect(reverse('login'))
    else:
        return HttpResponse(template.render(context, request))

#This code displays the search results form.
def results(request):
    screens = screenbooks.objects.all().values()
    print(screens)

    if request.POST:
        #sort = str(request.POST['sort'])
        search = str(request.POST['property__search']).lower()
        print(search)
        if search != '':
            screens = screenbooks.objects.all().values().filter(screenname__contains=search) #| screenbooks.objects.all().values().filter(description__contains=search)
            #return HttpResponseRedirect(reverse('index'))
        #elif search == 'screenname':
            #screens = screenbooks.objects.all().values().order_by('screenname')
        #elif search == 'description':
            #screens = screenbooks.objects.all().values().order_by('description')
        else:
            screens = screens
            return HttpResponseRedirect(reverse('index'))
    reQ = request.session.get('username').upper()
    print(reQ)
    template = loader.get_template('results.html')
    context = {
        'screens':screens,
        'reQ':reQ,
        'username': request.session.get('username')
    }

    if reQ == None:
        return HttpResponseRedirect(reverse('login'))
    else:
        return HttpResponse(template.render(context, request))
    #return HttpResponse(template.render(context, request))  

def property_details(request, id):
    print(id)
    details = screenbooks.objects.values().get(id=id)
    print(details)
    template = loader.get_template('property-details.html')
    context = {
        'details':details
    }
    return HttpResponse(template.render(context, request))