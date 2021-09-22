f=open("c:\\data\\funnyjokes.txt","r")
f_out=open("c:\\data\\funnyjokesreplica.txt","w")
for line in f:
    tokans=line.split(' ')
    f_out.write(line+str(len(tokans)))
f.close()
f_out.close()