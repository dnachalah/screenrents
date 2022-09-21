'''
        pictures = request.FILES
        print("picture files =",pictures.keys())
        k=0
        r = time.time()
        for i in pictures.keys():
            print(i)
            for j in pictures[i]:
                print("picture =",j)
                #j.append(str(r) + str(k))

        print("end =")

        #jpic = j
        print("jpic =",jpic)
        '''

        '''
        qdict = QueryDict('', mutable=True)
        qdict.update(pictures)
        print("qdict =",qdict)
        print("length of pictures =",len(pictures))
        print("length of qdict =",len(qdict))
        screenpic = qdict['screen__picture[]']
        print("screenpic =",screenpic)
        '''

        '''
            
            q = request.session['admin_id']
            r = time.time()
            print(r)
            h = str(r) + '-' + str(q)
            print(h)
            
            filee = fsss.save('screens/'+str(h), fh)
            #x = x.read()
            #print(x)
            
        
        #picture = j
        #print("picturej =",picture)
        fsss = FileSystemStorage()
        q = request.session['admin_id']
        filee = fsss.save('screens/'+str(h), f)
        filee_url = fsss.url(filee)
        '''

        '''
    mymembers = Rentalsapp.objects.all().values()
    print('mymembers =',mymembers)
    details = screens.objects.all().values()
    print(details)
    print('id = ',id)
    admins = admin.objects.all().values()
    print(admins)
    z = request.session.get('admin_id')
    print(z)
    adminn = admin.objects.values().get(id=z)
    print(adminn)
    screen = screens.objects.all().values().get(id=id)
    print(screen)
    pp = request.session.get('profilepic')
    print('profile = ',pp)
    reQ = request.session.get('username').upper()
    print('reQ =',reQ)

    print("Ben")
    '''

'''
<div class="col-md-6 col-lg-4 gallery__single__two">
<a href="{% static 'assets/images/gallery/two.png' %}">
<img src="{% static 'assets/images/gallery/two.png' %}" alt="Property Image">
</a>
</div>
<div class="col-md-6 col-lg-4 gallery__single__two">
<a href="{% static 'assets/images/gallery/three.png' %}">
<img src="{% static 'assets/images/gallery/three.png' %}" alt="Property Image">
</a>
</div>
<div class="col-md-6 col-lg-4 gallery__single__two">
<a href="{% static 'assets/images/gallery/four.png' %}">
<img src="{% static 'assets/images/gallery/four.png' %}" alt="Property Image">
</a>
</div>
<div class="col-md-6 col-lg-4 gallery__single__two">
<a href="{% static 'assets/images/gallery/five.png' %}">
<img src="{% static 'assets/images/gallery/five.png' %}" alt="Property Image">
</a>
</div>
<div class="col-md-6 col-lg-4 gallery__single__two">
<a href="{% static 'assets/images/gallery/six.png' %}">
<img src="{% static 'assets/images/gallery/six.png' %}" alt="Property Image">
</a>
</div>
<div class="col-md-6 col-lg-4 gallery__single__two">
<a href="{% static 'assets/images/gallery/seven.png' %}">
<img src="{% static 'assets/images/gallery/seven.png' %}" alt="Property Image">
</a>
</div>
<div class="col-md-6 col-lg-4 gallery__single__two">
<a href="{% static 'assets/images/gallery/eight.png' %}">
<img src="{% static 'assets/images/gallery/eight.png' %}" alt="Property Image">
</a>
</div>
<div class="col-md-6 col-lg-4 gallery__single__two">
<a href="{% static 'assets/images/gallery/nine.png' %}">
<img src="{% static 'assets/images/gallery/nine.png' %}" alt="Property Image">
</a>
</di
'''

'''
def content_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s_%s.%s" % (instance.user.id, instance.questid.id, ext)
    return os.path.join('uploads', filename)
'''