#Name: Tzu-Chuan Chu
#Assignment Number: 4
#Date: 10/11/18
#Section: 8:00-9:30
#Description: This program is written for Super Cool T-Shirts.
#Description: This program takes orders for two different colored shirts and calculates costs
#Description: This program can also give away free shirts and calculate donation amounts.

#Defining function main()
def main():
    #Declaring T-shirt prices
    REDPRICE = 6.00
    YELLOWPRICE = 19.50

    #Declaring max number of shirts per order
    MAXREDSHIRT = 10
    MAXYELLOWSHIRT = 12

    #Declaring tax and donation percentage
    TAX = .075
    DONATION = .02

    #Declaring inital values for number of shirts
    totalRed = 0
    totalYellow = 0

    #Declaring initial values for total cost
    redTotalCost = 0
    yellowTotalCost = 0

    #Initializing loop
    choice = 'y'
    while choice == 'Y' or choice == 'y':
        #Calling function displayMenu()
        displayMenu()
        #Assigning variable to result of function getCustomerSelection()
        color = getCustomerSelection()
        #Decision making if shirt choice is red
        if color == 'R' or color == 'r':
            #Assigning variable to result of function getTShirtNumber()
            shirtNumber = getTShirtNumber(MAXREDSHIRT)
            #Accumulating total number of red shirts
            totalRed = totalRed + shirtNumber
            #Assigning variable to result of function calculateCharge()
            orderCost = calculateCharge(shirtNumber,REDPRICE,TAX)
            #Accumulating total cost of red shirts
            redTotalCost = redTotalCost + orderCost
        #Decision making if shirt choice is yellow
        else:
            #Assigning variable to result of function getTShirtNumber()
            shirtNumber = getTShirtNumber(MAXYELLOWSHIRT)
            #Accumulating total number of yellow shirts
            totalYellow = totalYellow + shirtNumber
            #Assigning variable to result of function calculateCharge()
            orderCost = calculateCharge(shirtNumber,YELLOWPRICE,TAX)
            #Accumulating total cost of yellow shirts
            yellowTotalCost = yellowTotalCost + orderCost

        #Calculating total number of shirts and total cost of order
        totalShirts = totalRed + totalYellow
        totalCost = redTotalCost + yellowTotalCost

        #Calling function buyMore()
        buyMore(totalShirts)

        #Prompting for another order
        choice = input('Do you want to continue shopping? (Y/y - yes) ')
        print()
        
        #Calculating donation amount
        donationAmount = (totalCost / (1 + TAX)) * DONATION

    #Displaying sales report    
    print('Sales Report')
    print('========================')
    #Displaying shirts sold and shirt costs
    print(format(totalRed,'4'),'red shirt(s)\t $',format(redTotalCost,'6.2f'))
    print(format(totalYellow,'4'),'yellow shirt(s)\t $',format(yellowTotalCost,'6.2f'))
    print(format(totalShirts,'4'),'total shirt(s)\t $',format(totalCost,'6.2f'))
    print()

    #Displaying donation amount
    print('Thank you for your purchase! '
          '$',format(donationAmount,'.2f'),' will be donated to United Way.',sep='')
    if totalShirts >= 5:
        print('You will also receive a free red shirt!')
    
        
#Defining function displayMenu()
def displayMenu():
    print('Welcome to Super Cool T-Shirts!')
    print('=================================\n')
    print('R/r - Red T-Shirt -- $6.00')
    print('Y/y - Yellow T-Shirt -- $19.50')
    print()

#Defining function getCustomerSelection()
def getCustomerSelection():
    #Prompting customer for shirt type
    shirtType = input('Which shirt would you like to order? (R - red, Y - yellow) ')
    #Validation loop for shirt type
    while shirtType != 'R' and shirtType != 'r' and shirtType != 'Y' and shirtType != 'y':
        print('Invalid type.')
        shirtType = input('Please enter another shirt type. ')
    #Returning result back to function main()
    return shirtType

#Defining function getTShirtNumber()
def getTShirtNumber(maxNumber):
    #Prompting for number of shirts
    shirtNumber = int(input('How many shirts would you like? '))
    #Validation loop for number of shirts
    while shirtNumber < 1 or shirtNumber > maxNumber:
        print('Invalid number.')
        if shirtNumber < 1:
            print('Number entered is negative or zero.\n')
        else:
            print('Number entered exceeded maximum number allowed.\n')
        shirtNumber = int(input('Please enter another number. '))
    print('You have just purchased',shirtNumber,'shirts.')
    #Returning result back to function main()
    return shirtNumber

#Defining function calculateCharge()
def calculateCharge(number,price,tax):
    #Calculation for total cost
    totalCost = (number * price) * (1 + tax)
    #Returning result to function main()
    return totalCost

#Defining function buyMore()
def buyMore(total):
    #Decision making if free shirt requirement isn't met
    if total > 1 and total < 5:
        print('If you buy',(5 - total),'more, you will receive a free red shirt!\n')
    #Decision making if free shirt requirement is met
    else:
        print('You have purchased',total,'total shirts.')
        print('You will receive a free red shirt!\n')
    
#Calling function main()    
main()
