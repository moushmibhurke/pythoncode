def calculate_total(exp):
    total=0
    for item in exp:
        total=total+item
    return total
tom_exp_list=[2100,3200,4500]
joe_exp_list=[2300,4500,2300]
toms_total=calculate_total(tom_exp_list)
print("tom's total is:",toms_total)
joes_total=calculate_total(joe_exp_list)
print("joe's total is:",joes_total)