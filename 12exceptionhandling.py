x=input("enter any number:")
y=input("enter any number:")
try:
   z= x / int(y)
except ZeroDivisionError as e:
    print("exception occured:division by zero")
    z= None
#except Exception as e:
    #print("exception type:",type(e).__name__)
except TypeError as e:
    print("type error exception")
    z= None
print("division is:",z)
