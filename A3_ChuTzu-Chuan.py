#Name: Tzu-Chuan Chu
#Assignment Number: 3
#Date: 9/27/18
#Section: 8:00 - 9:30
#Description: This program is designed for Mrs. Kate of Delectable Cakes to process orders.
#Description: This program also allows inventory to update itself as sales occur and calculates the profit made from sales.

#Setting prices for each flavor of cake
STRAWBERRYPRICE = 6.50
VANILLAPRICE = 8.00
CHOCOLATEPRICE = 6.50

#Setting the profit margin in percent for each cake
STRAWBERRYPROFITMARGIN = .10
VANILLAPROFITMARGIN = .20
CHOCOLATEPROFITMARGIN = .30

#Setting the initial inventory for each cake
STRAWBERRYINITIAL = 20
VANILLAINITIAL = 20
CHOCOLATEINITIAL = 20

#Setting the beginning inventory for validation loop
STRAWBERRYINVENTORY = 20
VANILLAINVENTORY = 20
CHOCOLATEINVENTORY = 20

#prompting for beginning of order
choice = input('Would you like to make an order? (Y or y for yes) ')

while choice == 'Y' or choice == 'y':
    #Outputting title of the store
    print('Welcome to Delectable Cakes!')
    print('============================\n')

    #Outputting menu of cakes
    print('S or s - Strawberry Sponge Cake')
    print('V or v - Vanilla Walnut Cake')
    print('C or c - Chocolate Raspberry Cake\n')

    #Prompting for the type of cake
    choiceType = input('Which cake would you like to buy? ')

    #Decision making for strawberry sponge cake
    if choiceType == 'S' or choiceType == 's':
        numberStrawberry = int(input('How many strawberry sponge cakes would you like? '))
        #Validation loop for strawberry sponge cake inventory
        while numberStrawberry > STRAWBERRYINVENTORY or numberStrawberry < 0:
            print('Invalid number.',STRAWBERRYINVENTORY,'cakes available. '+
                  'Please enter another number.')               
            numberStrawberry = int(input('How many strawberry sponge cakes would you like? '))
        #Updating strawberry sponge cake inventory
        STRAWBERRYINVENTORY = STRAWBERRYINVENTORY - numberStrawberry
        print(numberStrawberry,'strawberry sponge cakes have been sold.\n')

    #Decision making for vanilla walnut cake    
    elif choiceType == 'V' or choiceType == 'v':
        numberVanilla = int(input('How many vanilla walnut cakes would you like? '))
        #Validation loop for vanilla walnut cake inventory
        while numberVanilla > VANILLAINVENTORY or numberVanilla < 0:
            print('Invalid number.',VANILLAINVENTORY,'cakes available. '+
                  'Please enter another number.')
            numberVanilla = int(input('How many vanilla walnut cakes would you like? '))
        #Updating vanilla walnut cake inventory
        VANILLAINVENTORY = VANILLAINVENTORY - numberVanilla
        print(numberVanilla, 'vanilla walnut cakes have been sold.\n')

    #Decision making for chocolate raspberry cake    
    elif choiceType == 'C' or choiceType == 'c':
        numberChocolate = int(input('How many chocolate raspberry cakes would you like? '))
        #Validation loop for chocolate raspberry cake inventory
        while numberChocolate > CHOCOLATEINVENTORY or numberChocolate < 0:
            print('Invalid number.',CHOCOLATEINVENTORY,'cakes available. '+
                  'Please enter another number.')
            numberChocolate = int(input('How many chocolate walnut cakes would you like? '))
        #Updating chocolate raspberry cake inventory
        CHOCOLATEINVENTORY = CHOCOLATEINVENTORY - numberChocolate
        print(numberChocolate,'chocolate raspberry cakes have been sold.\n')

    #Outputting invalid statement for cake type    
    else:
        print('Invalid type.')
        
    #Prompting customer if they would like to make another order
    choice = input('Would you like to make another order?(Y or y for yes) ')
    print()

#Declaring end of order       
print('End of order.\n')

#Calculations for amount of each cake sold
strawberrySold = STRAWBERRYINITIAL - STRAWBERRYINVENTORY
vanillaSold = VANILLAINITIAL - VANILLAINVENTORY
chocolateSold = CHOCOLATEINITIAL - CHOCOLATEINVENTORY

#Calculation for total number of cakes sold
totalSold = strawberrySold + vanillaSold + chocolateSold

#Calculation for profit for each type of cake
strawberryProfit = (STRAWBERRYPRICE * STRAWBERRYPROFITMARGIN) * strawberrySold
vanillaProfit = (VANILLAPRICE * VANILLAPROFITMARGIN) * vanillaSold
chocolateProfit = (CHOCOLATEPRICE * CHOCOLATEPROFITMARGIN) * chocolateSold

#Calculation for total profit
totalProfit = strawberryProfit + vanillaProfit + chocolateProfit

#Outputting business report title
print('Business Report for Mrs. Kate')
print('============================\n')

#Outputting amount of cakes sold
print('You have sold',strawberrySold,'strawberry sponge cake(s).')
print('You have sold',vanillaSold,'vanilla walnut cake(s).')
print('You have sold',chocolateSold,'chocolate raspberry cake(s).')
print('You have sold a total of',totalSold,'cake(s).\n')

#Outputting the profit gained from cake sales
print('Your profit for strawberry sponge cake is $',format(strawberryProfit,'.2f'),'.',sep='')
print('Your profit for vanilla walnut cake is $',format(vanillaProfit,'.2f'),'.',sep='')
print('Your profit for chocolate raspberry cake is $',format(chocolateProfit,'.2f'),'.',sep='')
print('Your total profit is $',format(totalProfit,'.2f'),'.',sep='')






    
    
    
    
    


