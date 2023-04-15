"""
python func. that removes duplicates from an amount in a list and also sums up all the items and remove 7% VAT from that amount and print the amount
"""

#this list of items is stored in the variable

data = [350, 400, 250, 200, 150, 1000, 2000, 500, 1000, 500]

#removing the duplicate 
item = set(data)
print("this is the non-duplicated values: ", item)

#summation of non-duplicated list
Amount = sum(item)
print("this is the sum total of the amount: ", Amount)

#removal of 7% VAT from the amount
vat_deduction = 0.07 * Amount

#reminder print
Total = Amount - vat_deduction
print(Total)