from django.shortcuts import render
from array import array
from urllib import request
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Rentalsapp
from .models import admin
from .models import screens
from .models import contacts
from .models import screenbookings
from .models import subscription
from .models import categories
from .models import brands
from datetime import date
from datetime import datetime
from django.db.models import Q
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator
from . import views
from django.conf import settings
from django.http import QueryDict
from django.utils.datastructures import MultiValueDict
from mailjet_rest import Client
import requests
import urllib.request
import urllib.request as urllib
import json
import base64
import codecs
import io
import os
import time
# import the mailjet wrapper

# Get your environment Mailjet keys

# Create your views here.
def mailer(email_from, name_from, email_to, subject, message, adminjson,):
    API_KEY = "d3a921c220c205ae2a14f4ce4d3f545c"#os.environ["d3a921c220c205ae2a14f4ce4d3f545c"]
    API_SECRET = "23dc79679175647dd23ffc33e9f8f7ff"#os.environ["23dc79679175647dd23ffc33e9f8f7ff"]
    
    print(time.ctime())
    print("json=")
    print(adminjson)
    print(email_to)
    print(name_from)
   
    body = upload_file()
    bodyy = body.replace('%ssubject', str(subject))
    bodyy = bodyy.replace('%sbody', str(message))
    bodyy = bodyy.replace('%sProxynet', str(settings.APP_NAME))
    body = bodyy
    mailjet = Client(auth=(API_KEY, API_SECRET), version='v3.1')
    data = {
      'Messages': [
        {
          "From": {
            "Email": "sales@proxynetgroup.com",
            "Name": name_from,
          },
          "To": [
            {
              "Email": email_to,
              "Name": "You"
            }
          ],
          "Cc": [],
          "Bcc": adminjson,
          "Subject": subject,
          "TextPart": "Greetings from Mailjet!",
          "HTMLPart": body,
        }
      ]
    }
    print("Hello! Hello!!")
    print("body =", body)
    result = mailjet.send.create(data=data)
    print (result.status_code)
    print (result.json())

def admin_login(request):
    #form = Rentalsapp.objects.all().values()
    template = loader.get_template('admin_login.html')
    #context = {
        #'form': form,
    #}
    #return HttpResponse(template.render(context, request))
    return HttpResponse(template.render({}, request))

def admin_loginlog(request):
    email = request.POST.get('admin__login__email')
    y = request.POST.get('admin__login__pass')
    error ="";


    try:
        admins = admin.objects.all().values()
        print(admins)
        print(email)
        print(y)
        match = admin.objects.get(email=email,password=y)
        print("here")
        print(match.email)
        print(match.password)
        request.session['admin_id'] = match.id
        request.session['username'] = match.firstname
        req = request.session['username']
        print("username =",req)
        if req != None:
            del request.session['username']
        else:
            pass

    except Rentalsapp.DoesNotExist:
        template = loader.get_template('admin_login.html')
        context = {
            'error': "Invalid username or password.",
        }
        return HttpResponse(template.render(context, request))
    return HttpResponseRedirect(reverse('adminprofile'))

def admin_logout(request):
    try:
        del request.session['member_id']
        del request.session['username']
        template = loader.get_template('login.html')
        context = {
            'error': "Admin, you're logged out.",
        }
        return HttpResponse(template.render(context, request))
    except KeyError:
        pass

    return HttpResponseRedirect(reverse('admin_login'))

def adminprofile(request):
    admins = admin.objects.all().values()
    print('admins =',admins)
    z = request.session.get('admin_id')
    print('z =',z)
    if z != None:
        adminn = admin.objects.values().get(id=z)
        print('adminn =',adminn)
        adminnn = adminn['firstname']
        print(adminnn)
    else:
        z = z
    print('z =',z)
    if z == None:
        return HttpResponseRedirect(reverse('admin_login'))
    else:
        details = screens.objects.all().values()
        print("details =",details)

        categorys = categories.objects.all().values()
        brandds = brands.objects.all().values()
        print("category =", categorys)
        print("brandds =", brandds)
        
        year = date.today().year
        print(year)

        for y in details:
            pp = y['picture']
            print("pic=",pp)
            ppl = list(pp.split(","))
            print("pplist =", ppl)
            yfirst = ppl[0]
            print("yfirst =", yfirst)
            y['first']=yfirst
        print("ydetails =",details)
        screendetails = screenbookings.objects.all().values()
        mymembers = Rentalsapp.objects.all().values()
        print('mymembers =',mymembers)
        detailss = []
        users = []

        for x in screendetails:
            print('x =',x)
            h = x['id']
            p = x['screen_id']
            print("p =",p)
            detailss = screens.objects.all().values().get(id=x['screen_id'])
            print("detailss =", detailss)
            users = Rentalsapp.objects.all().values().get(id=x['user_id'])
            print('users =',users)
            x['firstname'] = users['firstname']
            x['screenname'] = detailss['screenname']
            print(x['firstname'], x['screenname'])
        print("Hello world!")
        print(screendetails)

        if request.method == "POST" and request.FILES:
            filee_ = []
            for count, x in enumerate(request.FILES.getlist("files")):
                print ("count=",count)
                print ("x=",x)
                fsss = FileSystemStorage()
                q = request.session['admin_id']
                r = time.time()
                print(r)
                h = str(r) + '-' + str(q) + '-' + str(count)
                print(h)
                filee = fsss.save('screens/' + str(h), x)
                print(filee)
                filee_url = fsss.url(filee)
                print(filee_url)
                filee_.append(filee_url)

            file_ = filee_
            fillee = ",".join(file_)
            print(fillee)

            a = request.POST['screen__name']
            b = fillee
            c = request.POST['price']
            d = request.POST['screen__description']
            e = date.today()
            f = request.POST['added__by']
            g = request.POST['screen__cat']
            print("gg =",g)
            h = request.POST['brand']
            print("hh =",h)
            i = request.POST['dimension']
            j = request.POST['quantity']
            k = request.POST['short__description']
            #n = request.POST['id']

            print("pictures =",b)

            if screens.objects.filter(screenname=a).exists():
                template = loader.get_template('admin_profile.html')
                context = {
                    'error': 'This screenname has been used before.',
                    #'username': request.session.get('username'),
                    'adminn': adminn,
                    'admins':admins,
                    'adminnn':adminnn,
                    'screendetails':screendetails,
                    'details':details,
                    'detailss':detailss,
                    'users':users,
                    'mymembers':mymembers,
                    'categorys':categorys,
                    'brandds':brandds,
                }
            else:
                details = screens(screenname=a, picture=b, price=c, description=d, date_added=e, added_by=f, category_id=g, brand_id=h, dimension=i, quantity=j, short_description=k,) #profile_picture=e)
                details.save()
                print("here")
                print("screens =",details)
                return HttpResponseRedirect(reverse('adminprofile')+'#addscreens')

        else:
            template = loader.get_template('admin_profile.html')
            context = {
                'error': '',
                'adminnn':adminnn,
                #'imgscreen':imgscreen,
                #'imgscreen1':imgscreen1,
                #'username': request.session.get('username'),
                'adminn': adminn,
                'admins':admins,
                'screendetails':screendetails,
                'details':details,
                'detailss':detailss,
                'users':users,
                'year':year,
                'mymembers':mymembers,
                'categorys':categorys,
                'brandds':brandds,
            }
            return HttpResponse(template.render(context, request))

def remove_screens(request, id=""):
    admins = admin.objects.all().values()
    print('admins =',admins)
    z = request.session.get('admin_id')
    print('z =',z)
    if z != None:
        adminn = admin.objects.values().get(id=z)
        print('adminn =',adminn)
        adminnn = adminn['firstname']
        print(adminnn)
    else:
        z = z
    print('z =',z)
    if z == None:
        return HttpResponseRedirect(reverse('admin_login'))
    else:    
        pid = request.session['pic__id']
        if request.POST:
            a = request.POST['pic__id']
            request.session['pic__id'] = a
            pid = request.session['pic__id']
            print("pid =", pid)
            if id == "":
                id = pid
                print('id from pid =',id)
            else:
                id = id
                print('id from pid2 =',id)
            mymembers = Rentalsapp.objects.all().values()
            print('mymembers =',mymembers)
            print('id =',id)
            details = screens.objects.all().values()
            print(details)
            detailss = screens.objects.values().get(id=id)
            picz = detailss['picture']
            piczz = picz.split(",")
            print("piczz =", piczz)
            year = date.today().year
            print(year)
            pp = request.session.get('profilepic')
            print('profile =', pp)

            template = loader.get_template('remove_screens.html')
            print("Total = ",len(piczz))
            context = {
                #'screendetails':screendetails,
                'mymembers':mymembers,
                'adminn': adminn,
                'adminnn':adminnn,
                'admins':admins,
                'pp':pp,
                'year':year,
                'details':details,
                'piczz':piczz,
                'detailss':detailss,        
                #'o':o,

                'error': '',
            }
            return HttpResponse(template.render(context, request))
        elif request != "POST" and pid != '':
            id = pid
            print('id from pid3 =',id)
            mymembers = Rentalsapp.objects.all().values()
            details = screens.objects.all().values()
            detailss = screens.objects.values().get(id=id)
            picz = detailss['picture']
            piczz = picz.split(",")
            year = date.today().year
            print(year)
            admins = admin.objects.all().values()
            z = request.session.get('admin_id')
            adminn = admin.objects.values().get(id=z)
            adminnn = adminn['firstname']
            pp = request.session.get('profilepic')
            template = loader.get_template('remove_screens.html')
            print("Total = ",len(piczz))
            context = {
                #'screendetails':screendetails,
                'mymembers':mymembers,
                'adminn': adminn,
                'adminnn':adminnn,
                'admins':admins,
                'pp':pp,
                'details':details,
                'piczz':piczz,
                'detailss':detailss,
                'year':year,        
                #'o':o,

                'error': '',
            }
            return HttpResponse(template.render(context, request))
        else:
            return HttpResponseRedirect(reverse('adminprofile'))

def removescreendel(request, id):
    admins = admin.objects.all().values()
    print('admins =',admins)
    z = request.session.get('admin_id')
    print('z =',z)
    if z != None:
        adminn = admin.objects.values().get(id=z)
        print('adminn =',adminn)
        adminnn = adminn['firstname']
        print(adminnn)
    else:
        z = z
    print('z =',z)
    if z == None:
        return HttpResponseRedirect(reverse('admin_login'))
    else:
        print('id =', id)
        screen = screens.objects.values().get(id=id)
        print('screenz =', screen)
        delpic = screen['picture']
        print('delpic =', delpic)
        delpics = delpic.split(",")
        print('delpics =', delpics)
        mymembers = Rentalsapp.objects.all().values()
        print('mymembers =',mymembers)
        print('id =',id)
        details = screens.objects.all().values()
        print(details)
        detailss = screens.objects.values().get(id=id)
        picz = detailss['picture']
        piczz = picz.split(",")
        print("piczz =", piczz)
        year = date.today().year
        print(year)
        admins = admin.objects.all().values()
        print('admins =',admins)
        pp = request.session.get('profilepic')
        print('profile =', pp)
        if request.POST:
            a = request.POST['pic__url']
            print('pic_url =',a)
            #print('delpic =', delpic)
            if a in delpics:
                delpics.remove(a)
                print('delpics dict after removal =',delpics)
                delpics = ",".join(delpics)
                print('delpics string after removal =',delpics)
                screen = screens(id=screen['id'], screenname=screen['screenname'], picture=delpics, price=screen['price'], description=screen['description'], date_added=screen['date_added'], added_by=screen['added_by'], updated_by=screen['updated_by']) #profile_picture=e)
                print("picturel =", delpics)
                screen.save()
                print("screens =",screen)
                template = loader.get_template('remove_screens.html')
                print("Total = ",len(piczz))
                context = {
                    #'screendetails':screendetails,
                    'mymembers':mymembers,
                    'adminn': adminn,
                    'adminnn':adminnn,
                    'admins':admins,
                    'year':year,
                    'pp':pp,
                    'details':details,
                    'piczz':piczz,
                    'detailss':detailss,        
                    #'o':o,

                    'error': '',
                }
                print("Hello")
                #return HttpResponse(template.render(context, request))
                return HttpResponseRedirect(reverse('remove_screens'))
            else:
                return HttpResponseRedirect(reverse('remove_screens'))
        
        return HttpResponseRedirect(reverse('remove_screens'))

def userstatus(request, id):
    admins = admin.objects.all().values()
    print('admins =',admins)
    z = request.session.get('admin_id')
    print('z =',z)
    if z != None:
        adminn = admin.objects.values().get(id=z)
        print('adminn =',adminn)
        adminnn = adminn['firstname']
        print(adminnn)
    else:
        z = z
    print('z =',z)
    if z == None:
        return HttpResponseRedirect(reverse('admin_login'))
    else:
        mymembers = Rentalsapp.objects.all().values()
        print('mymembers =',mymembers)
        print('id = ',id)
        member = Rentalsapp.objects.values().get(id=id)
        print("member =", member)
        year = date.today().year
        print(year)
        pp = request.session.get('profilepic')
        print('profile = ',pp)
        template = loader.get_template('userstatus.html')
        context = {
            'mymembers':mymembers,
            'id':id,
            'pp':pp,
            'year':year,
            #'member':member,
            'adminnn':adminnn,
            'member':member,

            'error': '',
        }
        return HttpResponse(template.render(context, request))
    

def userstatusrecord(request,id):
    screendetails = screenbookings.objects.all().values()
    print(screendetails)
    mymembers = Rentalsapp.objects.all().values()
    print(mymembers)
    print('id = ',id)
    #details = screens.objects.values().get(id=id)
    #print(details)
    #k = request.session.get('member_id')
    member = Rentalsapp.objects.values().get(id=id)
    print(member)
    year = date.today().year
    print(year)
    screenns = screens.objects.all().values()
    print(screenns)
    pp = request.session.get('profilepic')
    print('profile = ',pp)
    details = screens.objects.all().values()
    print('details =',details)
    q = screenns
    admins = admin.objects.all().values()
    print('admins =',admins)
    z = request.session.get('admin_id')
    print('z =',z)
    if z != None:
        adminn = admin.objects.values().get(id=z)
        print('adminn =',adminn)
        adminnn = adminn['firstname']
        print(adminnn)
    else:
        z = z
    print('z =',z)
    if z == None:
        return HttpResponseRedirect(reverse('admin_login'))
    else:
        if request.POST:
            sort = request.POST['sort']
            print("Hello")
            if sort == 'Active':
                member = Rentalsapp(status=sort, firstname=member['firstname'], lastname=member['lastname'], email=member['email'], password=member['password'], id=member['id'], profile_picture=member['profile_picture'],)
                member.save()
                print('member with g =',member)
                
                for x in screendetails:
                    print(x)
                    p = x['screen_id']
                    print("p =",p)
                    g = x['user_id']
                    print("g =",g)
                    detailss = screens.objects.values().get(id=x['screen_id'])
                    print('detailss =',detailss)
                    x['screenname'] = detailss['screenname']
                    users = Rentalsapp.objects.all().values().get(id=x['user_id'])
                    print('users =',users)
                    x['firstname'] = users['firstname']
                    y = x['firstname'].upper()
                    print('user =',y)
                    print(x['screenname'])
                template = loader.get_template('admin_profile.html')
                context = {
                    'details':details,
                    'mymembers':mymembers,
                    #'error': 'You have successfully booked your order',
                    'member':member,
                    'pp':pp,
                    'year':year,
                    'adminnn': adminnn,
                    'adminn': adminn,
                    'admins':admins,
                    'screendetails':screendetails,
                    'detailss':detailss,
                    'users':users,
                }
                return HttpResponse(template.render(context, request))
            elif sort == 'Disabled':
                member = Rentalsapp(status=sort, firstname=member['firstname'], lastname=member['lastname'], email=member['email'], password=member['password'], id=member['id'], profile_picture=member['profile_picture'],)
                member.save()
                print('member with g =',member)

                for x in screendetails:
                    print(x)
                    p = x['screen_id']
                    print("p =",p)
                    g = x['user_id']
                    print("g =",g)
                    detailss = screens.objects.values().get(id=x['screen_id'])
                    print('detailss =',detailss)
                    x['screenname'] = detailss['screenname']
                    users = Rentalsapp.objects.all().values().get(id=x['user_id'])
                    print('users =',users)
                    x['firstname'] = users['firstname']
                    y = x['firstname'].upper()
                    print('user =',y)
                    print(x['screenname'])
                template = loader.get_template('admin_profile.html')
                context = {
                    'details':details,
                    'mymembers':mymembers,
                    #'error': 'You have successfully booked your order',
                    'member':member,
                    'pp':pp,
                    'adminnn': adminnn,
                    'adminn': adminn,
                    'admins':admins,
                    'screendetails':screendetails,
                    'detailss':detailss,
                    'users':users,
                }
                return HttpResponse(template.render(context, request))
            else:
                template = loader.get_template('admin_profile.html')
                context = {
                    'error': 'Date for return cannot be before date for pickup.',
                    'mymembers':mymembers,
                    'details':details,
                    'member':member,
                    'pp':pp,
                    'adminnn': adminnn,
                    'adminn': adminn,
                    'admins':admins,
                    'screendetails':screendetails,
                    'detailss':detailss,
                    'users':users,
                }
                return HttpResponse(template.render(context, request))
        else:
            return HttpResponseRedirect(reverse('userstatusrecord'))

def screensedit(request, id):
    admins = admin.objects.all().values()
    print('admins =',admins)
    z = request.session.get('admin_id')
    print('z =',z)
    if z != None:
        adminn = admin.objects.values().get(id=z)
        print('adminn =',adminn)
        adminnn = adminn['firstname']
        print(adminnn)
    else:
        z = z
    print('z =',z)
    if z == None:
        return HttpResponseRedirect(reverse('admin_login'))
    else:
        mymembers = Rentalsapp.objects.all().values()
        print('mymembers =',mymembers)
        details = screens.objects.all().values()
        print(details)
        print('id = ',id)
        screen = screens.objects.all().values().get(id=id)
        print(screen)
        catt = screen['category_id']
        brndd = screen['brand_id']
        print("catt =", catt)
        print("brndd =", brndd)
        year = date.today().year
        print(year)
        pp = request.session.get('profilepic')
        print('profile = ',pp)

        categorys = categories.objects.all().values()
        brandds = brands.objects.all().values()


        template = loader.get_template('addscreens.html')
        context = {
            'mymembers':mymembers,
            'details':details,
            'screen':screen,
            'year':year,
            'pp':pp,
            'adminnn':adminnn,
            'categorys':categorys,
            'brandds':brandds,
            'catt':catt,            
            'brndd':brndd,

            'error': '',
        }
        return HttpResponse(template.render(context, request))

def screenseditrecord(request,id):
    admins = admin.objects.all().values()
    print('admins =',admins)
    z = request.session.get('admin_id')
    print('z =',z)
    if z != None:
        adminn = admin.objects.values().get(id=z)
        print('adminn =',adminn)
        adminnn = adminn['firstname']
        print(adminnn)
    else:
        z = z
    print('z =',z)
    if z == None:
        return HttpResponseRedirect(reverse('admin_login'))
    else:
        screen = screens.objects.all().values().get(id=id)
        print("screen id =", screen['id'])
        print(screen)
        year = date.today().year
        print(year)
        #print("request.files =", request.FILES.getlist("files")) 

        if request.POST:
            if request.FILES:
                filee_ = []
                print("go here!")
                for count, x in enumerate(request.FILES.getlist("files")):
                    print("count = ", count)
                    print("here!!!")
                    print("x= ",x)
                    fsss = FileSystemStorage()
                    q = request.session['admin_id']
                    r = time.time()
                    print("time = ",r)
                    h = str(r) + '-' + str(q) + '-' + str(count)
                    print("screenname = ",h)
                    filee = fsss.save('screens/' + str(h), x)
                    print("filename =",filee)
                    filee_url = fsss.url(filee)
                    print("file_url =",filee_url)
                    filee_.append(filee_url)

                file_ = filee_
                fillee = ",".join(file_)
                print("screenpicurl =", fillee)
            else:
                fillee = screen['picture']

            a = request.POST['edit__screen__name']
            b = fillee
            c = request.POST['edit__price']
            d = request.POST['edit__screen__description']
            e = request.POST['edit__short__description']
            f = request.POST['updated__by']
            g = request.POST['edit__screen__cat']
            h = request.POST['edit__brand']
            i = request.POST['edit__dimension']
            j = request.POST['edit__quantity']
            n = screen['id']


            screen = screens(id=n, screenname=a, picture=b, price=c, description=d, date_added=screen['date_added'], added_by=screen['added_by'], updated_by=f, category_id=g, brand_id=h, dimension=i, quantity=j, short_description=e,) #(id=n, 
            print("screenname =", a)
            print("picturel =", b)
            print("price =", c)
            print("description =", d)
            print("short description =", e)
            print("updated by =", f)
            print("category =", g)
            print("brand =", h)
            print("dimension =", i)
            print("quantity =", j)
            screen.save()
            print("screens =",screen)
            #print(xx)
            return HttpResponseRedirect(reverse('adminprofile'))

        else:
            template = loader.get_template('admin_profile.html')
            context = {
                'error': '',
                'year':year,
                'adminnn':adminnn,
                #'username': request.session.get('username'),
                #'adminn': adminn,
                #'admins':admins,
                #'details':details,
                'screen':screen,
                #'mymembers':mymembers,
            }
            return HttpResponse(template.render(context, request))

def deletescreen(request, id):
    admins = admin.objects.all().values()
    print('admins =',admins)
    z = request.session.get('admin_id')
    print('z =',z)
    if z != None:
        adminn = admin.objects.values().get(id=z)
        print('adminn =',adminn)
        adminnn = adminn['firstname']
        print(adminnn)
    else:
        z = z
    print('z =',z)
    if z == None:
        return HttpResponseRedirect(reverse('admin_login'))
    else:
        screen = screens.objects.get(id=id)
        screen.delete()
        return HttpResponseRedirect(reverse('adminprofile'))

def statusedit(request, id):
    admins = admin.objects.all().values()
    print('admins =',admins)
    z = request.session.get('admin_id')
    print('z =',z)
    if z != None:
        adminn = admin.objects.values().get(id=z)
        print('adminn =',adminn)
        adminnn = adminn['firstname']
        print(adminnn)
    else:
        z = z
    print('z =',z)
    if z == None:
        return HttpResponseRedirect(reverse('admin_login'))
    else:
        mymembers = Rentalsapp.objects.all().values()
        print('mymembers =',mymembers)
        print('id = ',id)
        screendetails = screenbookings.objects.all().values().get(id=id)
        print(screendetails)
        screenns = screens.objects.all().values()
        print(screenns)
        details = screens.objects.values().get(id=screendetails['screen_id'])
        print("statusedit id details =", details)
        picz = details['picture']
        piczz = picz.split(",")
        print("piczz =", piczz)
        d = str(date.today())
        print(d)
        year = date.today().year
        print(year)
        pp = request.session.get('profilepic')
        print('profile = ',pp)
        template = loader.get_template('statusedit.html')
        context = {
            'screendetails':screendetails,
            'mymembers':mymembers,
            'adminn': adminn,
            'adminnn':adminnn,
            'admins':admins,
            'pp':pp,
            'year':year,
            'piczz':piczz,
            'details':details,

            'error': '',
        }
        return HttpResponse(template.render(context, request))

def statuseditrecord(request,id):
    details = screens.objects.all().values()
    print('details =',details)
    mymembers = Rentalsapp.objects.all().values()
    print('mymembers =',mymembers)
    admins = admin.objects.all().values()
    print('admins =',admins)
    z = request.session.get('admin_id')
    print('z =',z)
    if z != None:
        adminn = admin.objects.values().get(id=z)
        print('adminn =',adminn)
        adminnn = adminn['firstname']
        print(adminnn)
    else:
        z = z
    print('z =',z)
    if z == None:
        return HttpResponseRedirect(reverse('admin_login'))
    else:
        screendetails = screenbookings.objects.all().values().get(id=id)
        print(screendetails)
        print('id = ',id)
        k = request.session.get('member_id')
        print("k =", k)
        if k != None:
            member = Rentalsapp.objects.values().get(id=k)
        else:
            member = "None"
        print("member =",member)
        screenns = screens.objects.all().values()
        print(screenns)
        pp = request.session.get('profilepic')
        print('profile = ',pp)
        year = date.today().year
        print(year)
        q = screenns
        print("Ben")

        if request.POST:
            sort = request.POST['sort']
            print("Hello")
            if sort == 'Completed':
                screendetails = screenbookings(status=sort, date_for_pickup=screendetails['date_for_pickup'], date_for_return=screendetails['date_for_return'], date_added=screendetails['date_added'], screen_id=screendetails['screen_id'], id=screendetails['id'], user_id=screendetails['user_id'],)
                screendetails.save()
                print('screendetails with g =',screendetails)
                screendetails = screenbookings.objects.all().values()
                print('screendetails =',screendetails)

                for x in screendetails:
                    print(x)
                    p = x['screen_id']
                    print("p =",p)
                    g = x['user_id']
                    print("g =",g)
                    detailss = screens.objects.values().get(id=x['screen_id'])
                    print('detailss =',detailss)
                    x['screenname'] = detailss['screenname']
                    users = Rentalsapp.objects.all().values().get(id=x['user_id'])
                    print('users =',users)
                    x['firstname'] = users['firstname']
                    y = x['firstname'].upper()
                    print('user =',y)
                    #d = x['date_taken']
                    #e = x['date_returned']
                    #f = x['date_added']
                    print(x['screenname'])
                    subject = "Status of your order"
                    message = "Hello " + y + "!<br> Your order has been confirmed and completely processed."
                    #print(message)
                    email_from = ""
                    name_from = "PRORENT admin"
                    email_to = users['email']
                    print("check for them: ",subject, message, email_from, name_from, email_to)
                    mailer(email_from, name_from, email_to, subject, message,)
                template = loader.get_template('admin_profile.html')
                context = {
                    'details':details,
                    'mymembers':mymembers,
                    #'error': 'You have successfully booked your order',
                    'member': member,
                    'pp':pp,
                    'adminn': adminn,
                    'adminnn':adminnn,
                    'admins':admins,
                    'screendetails':screendetails,
                    'detailss':detailss,
                    'users':users,
                }
                return HttpResponse(template.render(context, request))

            elif sort == 'Pending':
                screendetails = screenbookings(status=sort, date_added=screendetails['date_added'], screen_id=screendetails['screen_id'], id=screendetails['id'], user_id=screendetails['user_id'],)
                screendetails.save()
                print('screendetails with g =',screendetails)
                screendetails = screenbookings.objects.all().values()
                print('screendetails =',screendetails)
            #b = screendetails['screen_id']
            #print(b)

                for x in screendetails:
                    print(x)
                    p = x['screen_id']
                    print("p =",p)
                    g = x['user_id']
                    print("g =",g)
                    detailss = screens.objects.values().get(id=x['screen_id'])
                    print('detailss =',detailss)
                    x['screenname'] = detailss['screenname']
                    users = Rentalsapp.objects.all().values().get(id=x['user_id'])
                    print('users =',users)
                    x['firstname'] = users['firstname']
                    y = x['firstname'].upper()
                    print('user =',y)
                    #d = x['date_taken']
                    #e = x['date_returned']
                    #f = x['date_added']
                    print(x['screenname'])
                template = loader.get_template('admin_profile.html')
                context = {
                    'details':details,
                    'mymembers':mymembers,
                    #'error': 'You have successfully booked your order',
                    'member': member,
                    'pp':pp,
                    'year':year,
                    'adminn': adminn,
                    'admins':admins,
                    'screendetails':screendetails,
                    'detailss':detailss,
                    'users':users,
                }
                return HttpResponse(template.render(context, request))
            else:
                template = loader.get_template('admin_profile.html')
                context = {
                    'details':details,
                    'mymembers':mymembers,
                    'error': 'Date for return cannot be before date for pickup.',
                    'pp':pp,
                    'adminn': adminn,
                    'adminnn':adminnn,
                    'admins':admins,
                    'screendetails':screendetails,
                    'detailss':detailss,
                    'users':users,
                    'year':year,
                    'member': member,
                }
                return HttpResponse(template.render(context, request))
        else:
            return HttpResponseRedirect(reverse('statuseditrecord'))

#This code displays the login form.
def login(request):
    form = Rentalsapp.objects.all().values()
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
    form = Rentalsapp.objects.all().values()
    error ="";


    try:
        mymembers = Rentalsapp.objects.all().values().order_by('lastname')
        print(mymembers)
        print(email)
        print(y)
        match = Rentalsapp.objects.get(email=email,password=y)
        print("here")
        print(match.email)
        print(match.password)
        request.session['member_id'] = match.id
        request.session['username'] = match.firstname
        req = request.session['username']
        print(req)

        z = request.session.get('admin_id')
        print(z)
        if z != None:
            del request.session['admin_id']
        else:
            pass

        #memid = request.session['member_id']
        #return HttpResponseRedirect(reverse('index'))
        mid = request.session.get('member_id')
        member = member = Rentalsapp.objects.values().get(id=mid)
        if member['status'] == "Disabled":
            template = loader.get_template('login.html')
            context = {
                'error': "Your account has been disabled.",
            }
            return HttpResponse(template.render(context, request))
        else:
            pass
    except Rentalsapp.DoesNotExist:
        template = loader.get_template('login.html')
        context = {
            'error': "Invalid username or password.",
        }
        return HttpResponse(template.render(context, request))
    return HttpResponseRedirect(reverse('index'))


def logout(request):
    try:
        del request.session['member_id']
        del request.session['username']
        template = loader.get_template('login.html')
        context = {
            'error': "You're logged out.",
        }
        return HttpResponse(template.render(context, request))
    except KeyError:
        pass

    return HttpResponseRedirect(reverse('login'))

def emailresetpass(request):
    template = loader.get_template('resetpassword.html')
    context = {
        'error': '',
    }
    return HttpResponse(template.render(context, request))

def emailresetpassrecord(request):
    if request.POST:
        a = str(request.POST['reset__email']).lower()

        if "@" in a:
            #...ensures inputed email hasn't been used before...
            try:
                match = Rentalsapp.objects.get(email=a)
                print("match =",match)
                namm = str(match.firstname).upper()
                mid = match.id
                print("match.name =",namm)

                subject = "Reset password"
                message = "Hello " + namm + '!<br> Forgot your login password?<br> <a href="http://127.0.0.1:8000/rentalsapp/resetpass/' + str(mid) + '">Click here</a> to set a new one.'
                #print(message)
                email_from = ""
                name_from = settings.APP_NAME
                email_to = a
                adminjson = [{"Email": "ayodelea@proxynetgroup.com", "Name": "Ayodele Adedayo"}]
                print("check for them: ",subject, message, email_from, name_from, email_to)
                mailer(email_from, name_from, email_to, subject, message, adminjson,)
                template = loader.get_template('check_your_email.html')
                context = {
                    'error': '',
                }
                return HttpResponse(template.render(context, request))
        
            #return HttpResponseRedirect(reverse('login'))

            except Rentalsapp.DoesNotExist:
                template = loader.get_template('resetpassword.html')
                context = {
                    'error': "This email doesn't exist. Please input a correct email.",
                }
                return HttpResponse(template.render(context, request))
                
        else:
            template = loader.get_template('resetpassword.html')
            context = {
                'error': 'Please enter a valid email',
            }
            return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect(reverse('emailresetpass'))

def resetpass(request, id):
    id = id
    template = loader.get_template('setnewpass.html')
    context = {
        'error': '',
        'id':id,
    }
    return HttpResponse(template.render(context, request))

def resetpassrecord(request, id):
    if request.POST:
        mymembers = Rentalsapp.objects.all().values()
        print(mymembers)
        
        try:
            member = Rentalsapp.objects.values().get(id=id)
            print("member =",member)

            match = Rentalsapp.objects.get(id=id)
            print("match =",match)
            namm = str(match.firstname).upper()
            mid = match.id
            i = request.POST['reset_pass']
            j = request.POST['con_reset_pass']
            print("i, j =",i, j)
            #k = request.POST['id']

            #member = Rentalsapp.objects.get(id=k)
            if i != j:
                template = loader.get_template('setnewpass.html')
                context = {
                    'error': 'Passwords do not match',
                    #'member': member
                }
                return HttpResponse(template.render(context, request))
            else:
                member = Rentalsapp(password=i) #id=k,)
                member.save()
                print("member2 =",member)
                print("new password =", member.password)
                return HttpResponseRedirect(reverse('login'))
        except Rentalsapp.DoesNotExist:
            template = loader.get_template('setnewpass.html')
            context = {
                'error': "This email doesn't exist. Please input a correct email.",
            }
            return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect(reverse('resetpass'))
        
    

def contact(request):
    k = request.session.get('member_id')
    print("k =", k)
    if k != None:
        member = Rentalsapp.objects.values().get(id=k)
    else:
        member = "None"
    print("member =",member)
    pp = request.session.get('profilepic')
    print('profile = ',pp)
    reQ = request.session.get('username')
    print(reQ)
    if reQ != None:
        reQ = reQ.upper()
    else:
        reQ = reQ
    print(reQ)
    year = date.today().year
    print(year)
    html = "contact"
    esub = request.session.get('errorsub')
    if esub == None:
        esub = ""
    else:
        esub = esub
    template = loader.get_template('contact.html')
    context = {
        'member': member,
        'reQ':reQ,
        'pp':pp,
        'year':year,
        'html':html,
        'errorsub': esub,
        #'error': 'Message sent',
    }
    return HttpResponse(template.render(context, request))

def contactrecord(request):
    reQ = request.session.get('username')
    print(reQ)
    if reQ != None:
        reQ = reQ.upper()
    else:
        reQ = reQ
    print(reQ)
    year = date.today().year
    print(year)
    contactss = contacts.objects.values().all()
    print(contactss)
    if request.POST:
        a = str(request.POST['ask__name']).lower()
        b = str(request.POST['ask__registration__email']).lower()
        c = str(request.POST['phone_number']).lower()
        d = str(request.POST['ask__subject'])
        e = str(request.POST['ask_message'])

        print('nawa ooo')
        print("contacts1 =",contactss)
        #print(c)


        contactss = contacts(name=a, email=b, phone=c, subject=d, message=e,)
        print("name =",a)
        contactss.save()
        print(contactss.message)
        subject = contactss.subject
        message = "from:<br/>" + contactss.email + "<br/><br/><br/>" + "Message:<br/>" + contactss.message
        print(message)
        email_from = str(contactss.email)
        name_from = str(contactss.name)
        email_to = "diaphorosnachalah40@gmail.com"
        adminjson = [{"Email": "ayodelea@proxynetgroup.com", "Name": "Ayodele Adedayo"}]
        print("check for them: ",subject, message, email_from, name_from, email_to)
        mailer(email_from, name_from, email_to, subject, message, adminjson,)
        html = "contact"
        esub = request.session.get('errorsub')
        if esub == None:
            esub = ""
        else:
            esub = esub
        #print("phone number =",contactss.phone)
        #print("done oooo, done.")
        return HttpResponseRedirect(reverse('contact'))
    else:
        template = loader.get_template('contact.html')
        context = {
            'error': '',
            'reQ':reQ,
            'year':year,
            'html':html,
            'errorsub': esub,
            #'username': request.session.get('username'),
            #'adminn': adminn,
            #'admins':admins,
            #'details':details,
            #'screen':screen,
            #'mymembers':mymembers,
        }
        return HttpResponse(template.render(context, request))

def about_us(request):
    k = request.session.get('member_id')
    print("k =", k)
    if k != None:
        member = Rentalsapp.objects.values().get(id=k)
    else:
        member = "None"
    print("member =",member)
    pp = request.session.get('profilepic')
    print('profile = ',pp)
    reQ = request.session.get('username')
    print(reQ)
    if reQ != None:
        reQ = reQ.upper()
    else:
        reQ = reQ
    print(reQ)
    year = date.today().year
    print(year)
    html = "about_us"
    esub = request.session.get('errorsub')
    if esub == None:
        esub = ""
    else:
        esub = esub
    template = loader.get_template('about_us.html')
    context = {
        'member': member,
        'reQ':reQ,
        'pp':pp,
        'html':html,
        'errorsub': esub,
        'year':year,
    }
    return HttpResponse(template.render(context, request))

#This code displays the record of members in the database.
def indexx(request):
    mymembers = Rentalsapp.objects.all().values()
    print(mymembers)

    if request.POST:
        categorry = str(request.POST['category'])
        brrand = str(request.POST['brand'])
        search = str(request.POST['property__search']).lower()
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
    print(reQ)
    if reQ != None:
        reQ = reQ.upper()
    else:
        reQ = reQ
    print(reQ)
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
        e = str(request.POST['status']).lower()

#...ensures password and comfirm password match...
        if c != d:
            template = loader.get_template('registration.html')
            context = {
                'error': 'Password does not match',
            }
            return HttpResponse(template.render(context, request))
        elif "@" in a:
            #...ensures inputed email hasn't been used before...
            try:
                match = Rentalsapp.objects.get(email=a)

                template = loader.get_template('registration.html')
                context = {
                    'error': "This email has been used. Try another one.",
                }
                return HttpResponse(template.render(context, request))

            except Rentalsapp.DoesNotExist:
                member = Rentalsapp(firstname=x, lastname=y, email=a, password=c, status=e,) #profile_picture=e)
                member.save()
                print(member)
            return HttpResponseRedirect(reverse('login'))
        else:
            template = loader.get_template('registration.html')
            context = {
                'error': 'Please enter a valid email',
            }
            return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect(reverse('index'))

def index(request):
    reQ = request.session.get('username')
    print(reQ)
    if reQ != None:
        reQ = reQ.upper()
    else:
        reQ = reQ
    print("index reQ =",reQ)
    mymembers = Rentalsapp.objects.all().values()
    print(mymembers)
    year = date.today().year
    print(year)

    k = request.session.get('member_id')
    print("k =", k)
    if k != None:
        member = Rentalsapp.objects.values().get(id=k)
    else:
        member = "None"
    print("member =",member)
    pp = request.session.get('profilepic')
    print('profile = ',pp)

    categorys = categories.objects.all().values()
    brandds = brands.objects.all().values()
    screenns = screens.objects.all().values()[:10]
    print("screenns =",screenns)
    for y in screenns:
        ppc = y['picture']
        print("pic=",ppc)
        ppl = list(ppc.split(","))
        print("pplist =", ppl)
        yfirst = ppl[0]
        print("yfirst =", yfirst)
        y['first']=yfirst
    print("yscreenns =",screenns)
    for f in screenns:
        print("fscreenns =", f)
        categoryss = categories.objects.values().get(id=f['category_id'])
        print("categoryss =", categoryss)
        fcategory = categoryss['category']
        branddss = brands.objects.values().get(id=f['brand_id'])
        fbrand = branddss['brand']
        f['category'] = fcategory
        f['brand'] = fbrand
        print("branddss =", branddss)
    print("fscreenns =",screenns)
    html = "index"
    esub = request.session.get('errorsub')
    if esub == None:
        esub = ""
    else:
        esub = esub
    template = loader.get_template('index.html')
    context = {
        'screenns':screenns,
        'reQ':reQ,
        'username': request.session.get('username'),
        'member':member,
        'mymembers':mymembers,
        'pp':pp,
        'year':year,
        'categorys':categorys,
        'brandds':brandds,
        'html':html,
        'errorsub': esub,
    }

    return HttpResponse(template.render(context, request))

#This code displays the search results form.
def results(request):
    id = ""
    mymembers = Rentalsapp.objects.all().values()
    print(mymembers)
    year = date.today().year
    print(year)
    mpp = request.session.get('profilepic')
    print('profile = ',mpp)
    categorys = categories.objects.all().values()
    brandds = brands.objects.all().values()
    screenns = screens.objects.all().values()
    print("screenns1 =",screenns)
    for y in screenns:
        pp = y['picture']
        print("pic=",pp)
        ppl = list(pp.split(","))
        print("pplist =", ppl)
        yfirst = ppl[0]
        print("yfirst =", yfirst)
        y['first']=yfirst
    print("yscreenns =",screenns)
    for f in screenns:
        print("fscreenns =", f)
        categoryss = categories.objects.values().get(id=f['category_id'])
        print("categoryss =", categoryss)
        fcategory = categoryss['category']
        branddss = brands.objects.values().get(id=f['brand_id'])
        fbrand = branddss['brand']
        f['category'] = fcategory
        f['brand'] = fbrand
        print("branddss =", branddss)
    print("fscreenns =",screenns)
    error = 'Input a search term'

    if request.POST:
        categorys = categories.objects.all().values()
        brandds = brands.objects.all().values()
        print("category =", categorys)
        print("brandds =", brandds)
        categorry = request.POST.get('select1')
        request.session['select1'] = categorry
        cat = request.session['select1']
        print("cat =", cat)
        print("categorry =", categorry)
        brrand = request.POST.get('select2')
        request.session['select2'] = brrand
        brnd = request.session['select2']
        print("brnd =", brnd)
        print("brrand =", brrand)
        search = str(request.POST['property__search']).lower()
        request.session['property__search'] = search
        srch = request.session['property__search']
        print("search =", search)
        if search != '' and categorry == 'Select Category' and brrand == 'Select Brand':
            print('yo')
            print("search1 =", search)
            screenns = screens.objects.filter(screenname__icontains=search).values() | screens.objects.filter(description__icontains=search).values()# & screens.objects.filter(category_id__exact=categorry).values() & screens.objects.filter(brand_id__exact=brrand).values()
            print("filtered screens =",screenns)
        elif search != '' and categorry != 'Select Category' and brrand == 'Select Brand':
            print('yo!')
            print("search2 =", search)
            screenns = screens.objects.filter(screenname__icontains=search).values() & screens.objects.filter(description__icontains=search).values() & screens.objects.filter(category_id__exact=categorry).values()# | screens.objects.filter(brand_id__exact=brrand).values()
            print("filtered screens =",screenns)
        elif search != '' and brrand != 'Select Brand' and categorry == 'Select Category':
            print('yo!!')
            print("search3 =", search)
            screenns = screens.objects.filter(screenname__icontains=search).values() & screens.objects.filter(description__icontains=search).values() & screens.objects.filter(brand_id__exact=brrand).values()# | screens.objects.filter(category_id__exact=categorry).values()
            print("filtered screens =",screenns)
        elif search != '' and brrand != 'Select Brand' and categorry != 'Select Category':
            print('yo!!')
            print("search3 =", search)
            screenns = screens.objects.filter(screenname__icontains=search).values() & screens.objects.filter(description__icontains=search).values() & screens.objects.filter(brand_id__exact=brrand).values() & screens.objects.filter(category_id__exact=categorry).values()
            print("filtered screens =",screenns)
        elif search == '' and categorry == 'Select Category' and brrand == 'Select Brand':
            print('yo!!!')
            print("search4 =", search)
        else:
            screenns = screenns
            print("elsescreennns =", screenns)
            return HttpResponseRedirect(reverse('index'))
    for y in screenns:
        pp = y['picture']
        print("pic=",pp)
        ppl = list(pp.split(","))
        print("pplist =", ppl)
        yfirst = ppl[0]
        print("yfirst =", yfirst)
        y['first']=yfirst
    print("yscreenns =",screenns)
    for f in screenns:
        print("fscreenns =", f)
        categoryss = categories.objects.values().get(id=f['category_id'])
        print("categoryss =", categoryss)
        fcategory = categoryss['category']
        branddss = brands.objects.values().get(id=f['brand_id'])
        fbrand = branddss['brand']
        f['category'] = fcategory
        f['brand'] = fbrand
        print("branddss =", branddss)
    print("fscreenns =",screenns)
    # Set up pagination
    p = Paginator(screenns, 10)
    page = request.GET.get('page')
    screenns = p.get_page(page)
    print("pagscrn =", screenns)
    reQ = request.session.get('username')
    print(reQ)
    if reQ != None:
        reQ = reQ.upper()
    else:
        reQ = reQ
    print(reQ)
    cat = request.session.get('select1')
    print("cat =", cat)
    '''
    if cat != "Select Category":
        categoryss = categories.objects.values().get(id=cat)
    else:
        cat = categoryss['category']
    print("cat2 =", cat)
    '''
    brnd = request.session.get('select2')
    print("brndd =", brnd)
    '''
    if brnd != "Select Brand":
        branddss = brands.objects.values().get(id=brnd)
    else:
        brnd = branddss['brand']
    print("brnd2 =", brnd)
    '''
    srch = request.session.get('property__search')
    print("search33 =", srch)
    html = "results"
    esub = request.session.get('errorsub')
    if esub == None:
        esub = ""
    else:
        esub = esub
    template = loader.get_template('results.html')
    context = {
        'screenns':screenns,
        'screenns':screenns,
        'reQ':reQ,
        'username': request.session.get('username'),
        'mymembers':mymembers,
        'pp':pp,
        'mpp':mpp,
        'year':year,
        'categorys':categorys,
        'brandds':brandds,
        'cat':cat,        
        'brnd':brnd,
        'id':id,
        'srch':srch,
        'html':html,
        'errorsub': esub,
        #'errorsub':'Enter a valid email',
    }
    return HttpResponse(template.render(context, request))

def property_details(request, id):
    try:
        mymembers = Rentalsapp.objects.all().values()
        print(mymembers)
        print(id)
        k = request.session.get('member_id')
        print("k =", k)
        if k != None:
            member = Rentalsapp.objects.values().get(id=k)
        else:
            member = "None"
        print("member =",member)
        year = date.today().year
        print(year)
        screenns = screens.objects.all().values()
        print(screenns)
        details = screens.objects.values().get(id=id)
        print(details)
        picz = details['picture']
        piczz = picz.split(",")
        print("piczz =", piczz)
        d = str(date.today())
        print(d)
        pp = request.session.get('profilepic')
        print('profile = ',pp)
        reQ = request.session.get('username')
        print(reQ)
        if reQ != None:
            reQ = reQ.upper()
        else:
            reQ = reQ
        html = "results"
        esub = request.session.get('errorsub')
        if esub == None:
            esub = ""
        else:
            esub = esub
        template = loader.get_template('property-details.html')
        context = {
            'details':details,
            'mymembers':mymembers,
            'member': member,
            'reQ':reQ,
            'pp':pp,
            'd':d,
            'piczz':piczz,
            'year':year,
            'html':html,
            'errorsub': esub,
        }
        return HttpResponse(template.render(context, request))
    except screens.DoesNotExist:
        return HttpResponseRedirect(reverse('index'))

def bookorder(request, id):
    try:
        pp = request.session.get('profilepic')
        print('profile = ',pp)
        reQ = request.session.get('username')
        print(reQ)
        if reQ != None:
            reQ = reQ.upper()
        else:
            return HttpResponseRedirect(reverse('login'))
        admins = admin.objects.all().values()
        print('admins =',admins)
        year = date.today().year
        print(year)
        mymembers = Rentalsapp.objects.all().values()
        print(mymembers)
        print('id = ',id)
        k = request.session.get('member_id')
        print("k =", k)    
        html = "results"
        esub = request.session.get('errorsub')
        if esub == None:
            esub = ""
        else:
            esub = esub
        if request.POST:
            if k != None:
                member = Rentalsapp.objects.values().get(id=k)
            else:
                member = "None"
            print("member =",member)
            details = screens.objects.values().get(id=id)
            print("bookeredit details =", details)
            h = request.POST['date__taken']
            i = request.POST['date__returned']
            j = request.POST['screen__id']
            l = request.session.get('member_id')
            m = date.today()
            n = request.POST['status']
            print("h =",h)
            print("i =",i)
            print("j =",j)
            print("i =",l)
            print("m =",m)
            print("n =",n)

            if h > i:
                template = loader.get_template('property-details.html')
                context = {
                    'error': 'Date for return cannot be before date for pickup.',
                    'details':details,
                }
                return HttpResponse(template.render(context, request))
            else:
                screendetails = screenbookings(date_for_pickup=h, date_for_return=i, screen_id=j, user_id=l, date_added=m, status=n,)
                screendetails.save()
                print("screendetails =",screendetails)
                adminl = []

                for x in admins:
                    admin1 = {}
                    admin1["Name"] = x['firstname']
                    admin1["Email"] = x['email']
                
                    adminl.append(admin1)

        
                adminjson = adminl#json.dumps(adminl)
                print(adminjson)
                print(time.ctime())
                print("yo!")
                #ad_maill = 
                #print("ad_maill =",ad_maill)
                z = str(member['firstname']).upper()
                y = str(member['lastname']).upper()
                print("admin firstname =",x['firstname'])
                print("member firstname =",z)
                print("member lastname =",y)
                print("details screenname =",details['screenname'])
                print("date for pickup =",h)
                print("date for return =",i)
                subject = "New order alert"
                message = "Hello!<br>" +  z + " " + y + " has just placed an order to rent the " + details['screenname'] + ", and will want to pick it up by " + h + " and return it, " + i + ".<br>Kindly check, confirm and process this order.<br> Thanks in anticipation."
                #print(message)
                email_from = member['email']
                name_from = settings.APP_NAME
                name_from2 = settings.APP_NAME
                message2 = "Hello " + z + " " + y + "!<br>Your order has been received and is being processed.<br>Thanks for always, cheers!"
                email_to2 = member['email']
                print("email2 =",email_to2)
                email_to = "diaphorosnachalah77@gmail.com"
                print("check for them: ",subject, message, email_from, name_from, email_to)
                mailer(email_from, name_from, email_to, subject, message, adminjson,)
                mailer(email_from, name_from2, email_to2, subject, message2, [])
                template = loader.get_template('property-details.html')
                context = {
                    'details':details,
                    'mymembers':mymembers,
                    'error': 'You have successfully booked your order',
                    'reQ':reQ,
                    'pp':pp,
                    'year':year,
                    'html':html,
                    'screendetails':screendetails,
                    'errorsub': esub,
                }
                if reQ == None:
                    return HttpResponseRedirect(reverse('login'))
                else:
                    return HttpResponse(template.render(context, request))
        else:
            return HttpResponseRedirect(reverse('property_details'))
    except screens.DoesNotExist:
        return HttpResponseRedirect(reverse('index'))

def bookorderedit(request, id):
    try:
        reQ = request.session.get('username')
        print(reQ)
        if reQ != None:
            reQ = reQ.upper()
        else:
            reQ = reQ
        print('reQ =',reQ)
        mymembers = Rentalsapp.objects.all().values()
        print('mymembers =',mymembers)
        print('id = ',id)
        k = request.session.get('member_id')
        print("k =", k)
        if k != None:
            member = Rentalsapp.objects.values().get(id=k)
        else:
            member = "None"
        print("member =",member)
        screenns = screens.objects.all().values()
        print(screenns)
        details = screens.objects.values().get(id=id)
        print('bkorderedit details =',details)
        picz = details['picture']
        piczz = picz.split(",")
        print("piczz =", piczz)
        d = str(date.today())
        print(d)
        screendetails = screenbookings.objects.all().values().get(screen_id=id)
        print("bookeredit screendetails =",screendetails)
        print(screendetails['id'])
        pp = request.session.get('profilepic')
        print('profile = ',pp)
        
        year = date.today().year
        print(year)
        html = "profile"
        esub = request.session.get('errorsub')
        if esub == None:
            esub = ""
        else:
            esub = esub
        template = loader.get_template('bookorderedit.html')
        context = {
            'details':details,
            'mymembers':mymembers,
            'member': member,
            'reQ':reQ,
            'pp':pp,
            'd':d,
            'year':year,
            'html':html,
            'errorsub': esub,
            'piczz':piczz,
            'screendetails':screendetails,
            'error': '',
        }

        if reQ == None:
            return HttpResponseRedirect(reverse('login'))
        else:
            return HttpResponse(template.render(context, request))
    except screens.DoesNotExist:
        return HttpResponseRedirect(reverse('index'))

def bookordereditrecord(request,id):
    try:
        reQ = request.session.get('username')
        print(reQ)
        if reQ != None:
            reQ = reQ.upper()
        else:
            reQ = reQ
        print('reQ =',reQ)
        if reQ == None:
            return HttpResponseRedirect(reverse('login'))
        else:
            mymembers = Rentalsapp.objects.all().values()
            print(mymembers)
            print('id = ',id)
            year = date.today().year
            print(year)
            admins = admin.objects.all().values()
            print('admins =',admins)
            k = request.session.get('member_id')
            print("k =", k)
            if k != None:
                member = Rentalsapp.objects.values().get(id=k)
            else:
                member = "None"
            print("memberbkedit =",member)
            screenns = screens.objects.all().values()
            print(screenns)
            details = screens.objects.values().get(id=id)
            print("bookorder id details =", details)
            picz = details['picture']
            piczz = picz.split(",")
            print("piczz =", piczz)
            d = str(date.today())
            print(d)
            screendetails = screenbookings.objects.all().values().get(screen_id=id)
            print(screendetails)
            print(screendetails['id'])
            pp = request.session.get('profilepic')
            print('profile = ',pp)
            html = "profile"
            esub = request.session.get('errorsub')
            if esub == None:
                esub = ""
            else:
                esub = esub
            if request.POST:
                l = request.POST['edit__date__taken']
                m = request.POST['edit__date__returned']
                n = request.POST.get('screen__id')
                o = request.session.get('member_id')
                #p = request.GET.get('date__added')
                q = screenns

                if l > m:
                    template = loader.get_template('bookorderedit.html')
                    context = {
                        'error': 'Date for return cannot be before date for pickup.',
                        'details':details,
                        'member': member,
                        'd':d,
                        'mymembers':mymembers,
                        'reQ':reQ,
                        'pp':pp,
                        'year':year,
                        'html':html,
                        'piczz':piczz,
                        'errorsub': esub,
                    }
                    return HttpResponse(template.render(context, request))
                else:
                    screendetails = screenbookings(date_for_pickup=l, date_for_return=m, screen_id=n, user_id=o, date_added=screendetails['date_added'], id=screendetails['id'], status=screendetails['status'])
                    screendetails.save()
                    print(screendetails)
                    adminl = []

                    for x in admins:
                        admin1 = {}
                        admin1["Name"] = x['firstname']
                        admin1["Email"] = x['email']
                    
                        adminl.append(admin1)

                
                    adminjson = adminl#json.dumps(adminl)
                    print(adminjson)
                    print(time.ctime())
                    print("yo2!")
                    #ad_maill = 
                    #print("ad_maill =",ad_maill)
                    z = str(member['firstname']).upper()
                    y = str(member['lastname']).upper()
                    print("member firstname =",z)
                    print("member lastname =",y)
                    print("details screenname =",details['screenname'])
                    print("date for pickup =",l)
                    print("date for return =",m)
                    subject = "Edit order alert"
                    message = "Hello!<br>" +  z + " " + y + " has just edited an order to rent the " + details['screenname'] + ", the new pick-up date is " + l + " and the new return date is " + m + ".<br>Kindly check, confirm and process this order.<br> Thanks in anticipation."
                    #print(message)
                    email_from = member['email']
                    name_from = settings.APP_NAME
                    name_from2 = settings.APP_NAME
                    message2 = "Hello " + z + " " + y + "!<br>Your edited order has been received and is being processed.<br>Thanks for always, cheers!"
                    email_to2 = member['email']
                    print("email2 =",email_to2)
                    email_to = "diaphorosnachalah77@gmail.com"
                    print("check for them: ",subject, message, email_from, name_from, email_to)
                    mailer(email_from, name_from, email_to, subject, message, adminjson,)
                    mailer(email_from, name_from2, email_to2, subject, message2, [])
                    template = loader.get_template('bookorderedit.html')
                    context = {
                        'details':details,
                        'mymembers':mymembers,
                        'error': 'You have successfully edited your order',
                        'member': member,
                        'reQ':reQ,
                        'pp':pp,
                        'd':d,
                        'year':year,
                        'html':html,
                        'piczz':piczz,
                        'errorsub': 'Successfully subscribed!',
                    }
                    return HttpResponse(template.render(context, request))
    except screens.DoesNotExist:
        return HttpResponseRedirect(reverse('index'))

def profile(request):
    mymembers = Rentalsapp.objects.all().values()
    print(mymembers)
    reQ = request.session.get('username')
    print(reQ)
    if reQ != None:
        reQ = reQ.upper()
    else:
        reQ = reQ
    print(reQ)
    year = date.today().year
    print(year)
    pp = request.session.get('profilepic')
    print('profile = ',pp)
    k = request.session.get('member_id')
    print("k =", k)
    if k != None:
        member = Rentalsapp.objects.values().get(id=k)
    else:
        member = "None"
    print("member =",member)
    details = screens.objects.all().values()
    print("details =",details)
    screendetails = screenbookings.objects.all().values().filter(user_id=k)
    print("screendetails =",screendetails)
    #b = screendetails['screen_id']
    if screendetails != "<QuerySet []>":
        for x in screendetails:
            print(x)
            p = x['screen_id']
            print("screen_id =",p)
            details = screens.objects.values().get(id=x['screen_id'])
            print(details)
            x['screenname'] = details['screenname']
            d = x['date_for_pickup']
            e = x['date_for_return']
            f = x['date_added']
            print(x['screenname'])
            print(d,e,f)


        #print(b)
        print(screendetails)
        html = "profile"
        esub = request.session.get('errorsub')
        if esub == None:
            esub = ""
        else:
            esub = esub
        err = request.session.get('error')
        if err == None:
            err = ""
        else:
            err = err
        template = loader.get_template('profile.html')
        context = {
            'error': err,
            'reQ':reQ,
            'username': request.session.get('username'),
            'member': member,
            'mymembers':mymembers,
            'screendetails':screendetails,
            'details':details,
            'pp':pp,
            'year':year,
            'html':html,
            'errorsub': esub,
        }

        if reQ == None:
            return HttpResponseRedirect(reverse('login'))
        else:
            return HttpResponse(template.render(context, request))
    else:
        html = "profile"
        esub = request.session.get('errorsub')
        if esub == None:
            esub = ""
        else:
            esub = esub
        err = request.session.get('error')
        if err == None:
            err = ""
        else:
            err = err
        template = loader.get_template('profile.html')
        context = {
            'reQ':reQ,
            'username': request.session.get('username'),
            'member': member,
            'mymembers':mymembers,
            'screendetails':screendetails,
            'details':details,
            'pp':pp,
            'year':year,
            'html':html,
            'error':err,
            'errorsub': esub,
        }

        if reQ == None:
            return HttpResponseRedirect(reverse('login'))
        else:
            return HttpResponse(template.render(context, request))

def cancelorder(request, id):
    try:
        reQ = request.session.get('username')
        print(reQ)
        if reQ != None:
            reQ = reQ.upper()
        else:
            reQ = reQ
        print('reQ =',reQ)
        if reQ == None:
            return HttpResponseRedirect(reverse('login'))
        else: 
            screendetailss = screenbookings.objects.values().get(id=id)
            print("script =", screendetailss)
            print("date_for_pickup =", screendetailss['date_for_pickup'])
            if request.POST:
                cancel = request.POST['status']
                print("cancel =", cancel)
                print("Hello")
                screendetails = screenbookings(status=cancel, added_by=screendetailss['date_added'], date_added=screendetailss['date_added'], date_for_pickup=screendetailss['date_for_pickup'], date_for_return=screendetailss['date_for_return'], screen_id=screendetailss['screen_id'], id=screendetailss['id'], user_id=screendetailss['user_id'],)
                screendetails.save()
                print('screendetails with g =',screendetails)
                screendetails = screenbookings.objects.all().values()
                print('screendetails2 =',screendetails)
                users = Rentalsapp.objects.all().values().get(id=screendetailss['user_id'])
                print('users =',users)
                y = users['firstname'].upper()
                print('user =',y)
                subject = "Cancellation of order by customer"
                message = y + "'s order has been canceled'"
                print(message)
                email_from = str(users['email'])
                name_from = str(users['firstname'])
                email_to = "diaphorosnachalah40@gmail.com"
                adminjson = [{"Email": "ayodelea@proxynetgroup.com", "Name": "Ayodele Adedayo"}]
                print("check for them: ",subject, message, email_from, name_from, email_to)
                mailer(email_from, name_from, email_to, subject, message, adminjson,)
                #print(nene)
                return HttpResponseRedirect(reverse('profile'))
            else:
                return HttpResponseRedirect(reverse('profile'))
    except screenbookings.DoesNotExist:
        return HttpResponseRedirect(reverse('index'))


def deleteorder(request, id):
    admins = admin.objects.all().values()
    print('admins =',admins)
    z = request.session.get('admin_id')
    print('z =',z)
    if z != None:
        adminn = admin.objects.values().get(id=z)
        print('adminn =',adminn)
        adminnn = adminn['firstname']
        print(adminnn)
    else:
        z = z
    print('z =',z)
    if z == None:
        return HttpResponseRedirect(reverse('admin_login'))
    else:
        screendetails = screenbookings.objects.get(id=id)
        screendetails.delete()
        return HttpResponseRedirect(reverse('adminprofile'))

#This code edits Username and Password
def editprofile(request):
    reQ = request.session.get('username')
    print(reQ)
    if reQ != None:
        reQ = reQ.upper()
    else:
        reQ = reQ
    print('reQ =',reQ)
    if reQ == None:
        return HttpResponseRedirect(reverse('login'))
    else: 
        mymembers = Rentalsapp.objects.all().values()
        print("This is",mymembers)
        year = date.today().year
        print(year)
        if request.method == "POST" and request.FILES['avatar_upload']:
            upload = request.FILES['avatar_upload']
            print(upload)
            fss = FileSystemStorage()
            k = request.session.get('member_id')
            file = fss.save('profilepic/'+str(k), upload)
            file_url = fss.url(file)
            request.session['profilepic'] = file_url
            e = request.POST['save__first__name']
            f = request.POST['save__last__name']
            g = request.POST['save_email']
            h = request.session.get('profilepic')
            print("picture = ",h)
            #k = request.POST['id']

            k = request.session.get('member_id')
            print("id =", k)
            if k != None:
                member = Rentalsapp(firstname=e, lastname=f, email=g, id=k, profile_picture=h)
                print("profile-picture: ",member.profile_picture)
                member.save()
                #member = Rentalsapp.objects.values().get(id=k)
            else:
                member = "None"
            print("member =",member)

            '''
            member = Rentalsapp(firstname=e, lastname=f, email=g, id=k, profile_picture=h)
            print("profile-picture: ",member.profile_picture)
            member.save()
            '''

            member = Rentalsapp.objects.values().get(id=k)
            print(member)

            html = "profile"
            esub = request.session.get('errorsub')
            if esub == None:
                esub = ""
            else:
                esub = esub
            return HttpResponseRedirect(reverse('profile'))
        else:
            return HttpResponseRedirect(reverse('index'))



def editprofilee(request):
    reQ = request.session.get('username')
    print(reQ)
    if reQ != None:
        reQ = reQ.upper()
    else:
        reQ = reQ
    print('reQ =',reQ)
    if reQ == None:
        return HttpResponseRedirect(reverse('login'))
    else: 
        mymembers = Rentalsapp.objects.all().values()
        print(mymembers)
        year = date.today().year
        print(year)
        h = request.POST['current_pass']
        i = request.POST['new_pass']
        j = request.POST['con_new_pass']
        #k = request.POST['id']

        #member = Rentalsapp.objects.get(id=k)
        if i != j:
            error = "Passwords do not match"
            request.session['error'] = error
            err = request.session['error']
            print("err =", err)
            return HttpResponseRedirect(reverse('profile'))
        else:
            try:
                #print(k)
                print(h)
                match = Rentalsapp.objects.get(password=h) #id=k,)
                print(match)

            except Rentalsapp.DoesNotExist:
                html = "profile"
                esub = request.session.get('errorsub')
                error = "Invalid password."
                request.session['error'] = error
                err = request.session['error']
                print("err =", err)
                return HttpResponseRedirect(reverse('profile'))
            member = Rentalsapp(password=i) #id=k,)
            member.save()
            return HttpResponseRedirect(reverse('index'))


#Ths code deletes members from the record.
def delete(request, id):
    member = Rentalsapp.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('indexx'))


def upload_file():
    file_ = open(os.path.join(settings.BASE_DIR, 'rentalsapp\\templates\\', 'email_template.html'))
    #with open(file_, 'r') as f2:
    filee_ = file_.read()
    print(filee_)
    #file_ = open(os.path.join(settings.BASE_DIR, 'email_template.html'))
    print("file =",filee_)
    print("url =",settings.TEMPLATE_DIR)
    return filee_

def subscribe_email(request, html):
    print("email html =",html)
    subemails = subscription.objects.all().values()
    if request.POST:
        a = str(request.POST['news__letter']).lower()
        print("print a =", a)

#...ensures password and comfirm password match...
        if "@" in a:
            #...ensures inputed email hasn't been used before...
            try:
                match = subscription.objects.get(email=a)
                errorsub = "You are already subscribed"
                request.session['errorsub'] = errorsub
                esub = request.session['errorsub']
                print("esub =", esub)

                return HttpResponseRedirect(reverse(html))

            except subscription.DoesNotExist:
                subemail = subscription(email=a,)
                subemail.save()
                print("subemail =",subemail)
            return HttpResponseRedirect(reverse(html))
        else:
            errorsub = 'Please enter a valid email'
            request.session['errorsub2'] = errorsub
            esub = request.session['errorsub']
            print("esub2 =", esub)
            return HttpResponseRedirect(reverse(html))
    else:
        return HttpResponseRedirect(reverse('index'))