month_list = ["January", "February", "March", "April", "May"]
expense_list = [2340, 2500, 2100, 3100, 2980]
e = input("Enter expense amount: ")
e = int(e)

month = 0
for i in range(len(expense_list)):
    if e == expense_list[i]:
        month = i
        break

if month != 0:
    print("You spent",e,"in",month_list[month])
else:
    print("You didn't spend",e, "in any month")
