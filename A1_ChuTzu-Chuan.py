#Name: Tzu-Chuan Chu
#Assignment Number: 1
#Date: 9/10/18
#Section: 8 - 9:30
#Description: This is a program designed to help Mrs. Mu with her store, Cute Mugs. This program helps her calculate each transaction.

#Declaring prices and tax

MUGPRICE = float(6.00)
IMAGEPRICE = float(2.50)
TAXRATE = float(.075)

#Declaring starting inventory

STARTINGINVENTORY = int(20)

#Displaying shop title

print('''WELCOME TO CUTE MUGS!
~~~~~~~~~~~~~~~~~~~~~''')

#Displaying menu

print('Orange Mugs: $',MUGPRICE)
print('Add An Image: $',IMAGEPRICE)
print('''One mug can only have one image!
''')

#Prompting order

mugsNumber = int(input('How many mugs would you like to order? '))
imagesNumber = int(input('How many images would you like to order? '))

#Calculating cost of order

totalMugCost = MUGPRICE * mugsNumber
totalImageCost = IMAGEPRICE * imagesNumber
baseCost = totalMugCost + totalImageCost

#Calculating tax

salesTax = TAXRATE * baseCost
totalCost = salesTax + baseCost

#Calculating profit and remaining inventory

profit = baseCost * float(.15)
remainingInventory = STARTINGINVENTORY - mugsNumber

#Displaying report title

print('''
BUSINESS REPORT FOR CUTE MUGS
~~~~~~~~~~~~~~~~~~~~~
''')

#Displaying the cost of the order

print('The price of',mugsNumber,'orange mugs is $',format(totalMugCost,'.2f'))
print('The price of',imagesNumber,'images is $',format(totalImageCost,'.2f'))
print('The total purchase price for this order is $',format(totalCost,'.2f'))

#Displaying tax, profit, and remaining inventory

print('The sales tax for this order is $',format(salesTax,'.2f'))
print('The profit from this order is $',format(profit,'.2f'))
print('The remaining inventory of orange mugs is',remainingInventory)







