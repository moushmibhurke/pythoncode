india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]
city1=input("enter the city1:")
city2=input("enter the city2:")
if city1 in india and city2 in india:
    print("these cites are in india")
elif city1 in pakistan and city2 in pakistan:
    print("these cities are in pakistan")
elif city1 in bangladesh and city2 in bangladesh:
    print("these cites are in bangladesh")
else:
    print("both cites are in diffrent countries")