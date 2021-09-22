keylocation="chair"
locations=["garage","livingroom","chair","closet"]
for i in locations:
    if i==keylocation:
        print("key is found in :",i)
        break
    else:
         print("key is not found in :",i)
