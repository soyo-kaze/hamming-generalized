def hamming(c):
    b,p,d = [],[],[]
    #c = input("enter data-word:")
    z = len(c)
    for x in c:
        b.append(x)
    for x in c:
        b[z-1] = x
        z-=1
    x,y,k,g = 0,0,0,0
    for i in range(70):
        if(2**x == i+1):
            p.append(i)
            x+=1
        else:
            d.append(i)
        if len(d) == len(b):
            break
    l = p + d
    pb = []
    print(len(l),p,d,l)
    for x in d:
        l[x] = b[y]
        y+=1
    for x in range(len(p)):
        x = []
        pb.append(x)
    for n in p:
        g = n
        while g<len(l):
            for v in range(int(n)+1):
                if g>=len(l):
                    break
                pb[k].append(int(l[g]))
                g+=1
            for c in range(int(n)+1):
                if g>=len(l):
                    break
                g+=1
        k+=1
    print(pb)
    m = 0
    for x in pb:
        h = x[1]
        a = 1
        if len(x)<3:
            if h == 0:
                l[p[m]] = 0
            else:
                l[p[m]] = 1
        else:
            while a<(len(pb[m])-1):
                h = h^x[a+1]
                a+=1        
            l[p[m]] = h
        m+=1
    for y in l:
        l[l.index(y)] = str(y)
    return "".join(l[::-1])

f = open("wir.txt",'r')
x = f.read()
f.close()
y = hamming(x)
f = open("red.txt",'w')
f.write(y)
f.close

