#program to calculate electricity bill
#First 100 units: ₹1.50 per unit
#200 units: ₹2.50 per unit
#300 units: ₹4.00 per unit
#Beyond 300 units: ₹6.00 per unit
def calculate_Electricity_bill(units):
    bill = 0;
    if units <= 100:
        bill = units * 1.5 
    elif units > 100 and units <= 200:
        bill = (100*1.5) + ((units- 100) * 2.5)
    elif units > 200 and units <= 300 :
        bill = (100*1.5) + (100*2.5) + ((units- 200) * 4)
    else: 
        bill = (100*1.5) + (100*2.5) + (100*4) + ((units- 300) * 6)
    return round(bill,2)
units = int(input ("Enter the number of units consumed:"))
total_bill = calculate_Electricity_bill(units)
print (f"Your Total electricity bill would be {total_bill} rupees.Thank you")
