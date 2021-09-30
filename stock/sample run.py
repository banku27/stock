def runme(x=1,y=2):
    x=x+y
    y+=1
    print(x,'$',y)
    return x,y
a,b=runme()
print(a,'#',b)
print(runme(a,b))
