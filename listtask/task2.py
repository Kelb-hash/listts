"""
python program that sums up all the list of 9 items, removes duplicates and prints the result
"""
list = [7, 8, 20, 8, 5, 3, 15, 14, 13]

#removal of duplicate
item = set(list)
print("this is the non-duplicated list", item)

#summation of all the items
summation = sum(item)   #summing
print("oTtal =", summation)     #printing the summation

