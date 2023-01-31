#Andrea Paniagua
#Carné 18733
#hoja de trabajo 1 metodos numericos
def Bisec(xl,xu,es,imax,xr,iter,ea):
    iter=0
    xrold=xr
    xr=(xl+xu)/2
    iter=iter+1
    if xr!=0:
        ea=abs((xr-xrold)/xr)*100
    test=function(xl)*function(xr)
    if test<0:
        xu=xr
    elif test>0:
        xl=xr
    else:
        ea=0
    if ea<es or iter>=imax:
        exit()
    Bisec=xr
    


