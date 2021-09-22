india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]
city=input("enter the city:")
if city in india:
    print(city,"this city is in india")
elif city in pakistan:
    print(city,"this city is in pakistan")
elif city in bangladesh:
    print(city,"this city is in bangladesh")
else:
    print(city,"this city is not in these three countries")