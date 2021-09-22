indian = ["samosa", "daal", "naan", "biryani"]
chinese = ["eggroll", "friedrice", "noodles", "manchawsoup"]
italian = ["pizza", "pasta", "risotto"]
dish = input("enter a dish name:")
if dish in indian:
    print(dish, ":this is an indian dish")
elif dish in chinese:
    print(dish, ":this dish is chinese dish")
elif dish in italian:
    print(dish, ":this dish is italian")
else:
    print(dish,":I don't know which cuisine this dish belongs to:")
