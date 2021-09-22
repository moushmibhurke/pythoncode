sugarlevel=input("please enter your sugar level:")
sugar=float(sugarlevel)
if sugar<80:
    print("Your sugar is low")
elif sugar>100:
    print("Your sugar is high")
else:
    print("Your sugar is normal")