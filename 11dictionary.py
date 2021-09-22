f=open("c://data//book.txt","r")
s=f.read()
import json
book=json.loads(s)
for person in book:
    print(book[person])
