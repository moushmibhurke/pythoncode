f=open("c:\\data\\funnyjokes.txt","w")
f.write("teacher:why you are late today?\nstudent:there was sign saying go slow school ahead")
f=open("c:\\data\\funnyjokes.txt","r")
for line in f:
    print(line)
f.close()
