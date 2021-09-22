result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
headcount=0
tailcount=0
for item in result:
    if item=="heads":
        headcount=headcount+1
    else:
        tailcount=tailcount+1
print("total heads:",headcount)
print("total tails:",tailcount)