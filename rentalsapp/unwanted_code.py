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