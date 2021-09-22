book={}
book['tom'] = {'name':'tom','address':'1 red street NY','Phone':678456723}
book['dick'] = {'name':'dick','address':'1 green street NY','Phone':456456723}
book['harry'] = {'name':'harry','address':'1 blue street NY','Phone':67856723}
import json
s=json.dumps(book)
print(s)
with open("c://data//book.txt","w") as f:
    f.write(s)