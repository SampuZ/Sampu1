
def bubblesort(a):   
    while True:
        Swaped=False;
        for i in range(0,len(a)-1):
            if a[i]>a[i+1]:
                a[i],a[i+1]=a[i+1],a[i]
                Swaped=True
        if not Swaped:
            return a

print bubblesort([4,3,1,2,5])
