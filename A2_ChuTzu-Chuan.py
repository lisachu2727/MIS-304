#Name: Tzu-Chuan Chu
#Assignment Number: 1
#Date: 9/19/18
#Section: 8:00 - 9:30
#Description: This program was written for Favorite Books. It's designed to specifiy customer's book orders.

#Declaring price of books
GREEKHEROES = float(20.99)
LITTLEMATH = float(15.99)
#Declaring tax rate
TAXRATE = float(.0825)

#Declaring discount rates
MEMBERDISCOUNT = float(.10)
SETDISCOUNT = float(.15)

#Declaring initial flag value
errorFlag = 0

#Outputting title of store
print('''Welcome to Favorite Books (FB)
===============================''')

#Outputting books menu
print('G - Greek Heroes 2-book set -- $',format(GREEKHEROES, '.2f'))
print('L - Little Math Genius -- $',format(LITTLEMATH, '.2f'))
print()

#Prompting customer for book choice
choice = input('Please enter the book you would like to buy: ')

#Decision making if customer chooses to buy Greek Heroes first
if choice == 'G':
#Prompting customer for quantity of books they would like to buy
    numberGreek = int(input('How many sets of Greek Heroes would you like to buy? (1 - 3) '))
#Condition to see if customer entered a valid number of books
    if numberGreek >= 1 and numberGreek <= 3:
#Prompting customer for membership status
        memberStatus = input('Are you a Learning Avenue Club member? (y - yes, n - no)? ')
        if memberStatus == 'y':
#Cost calculation if customer is a member/receives member discount
            costGreek = numberGreek * GREEKHEROES * (1 - MEMBERDISCOUNT) * (1 + TAXRATE)
#Price output if customer is a member/receives member discount
            print('The charge is $',format(costGreek,'.2f'))
        elif memberStatus == 'n' and numberGreek == 3:
#Cost calculation if customer is not a member but qualifies for set discount
            costGreek = (((numberGreek - 1) * GREEKHEROES) + (GREEKHEROES * (1 - SETDISCOUNT))) * (1 + TAXRATE)
#Price output if customer is not a member but qualifies for set discount
            print('The charge is $',format(costGreek,'.2f'))
        elif memberStatus == 'n':
#Cost calculation if customer does not qualify for any discounts
            costGreek = numberGreek * GREEKHEROES * (1 + TAXRATE)
#Price output if customer does not qualify for any discounts
            print('The charge is $',format(costGreek,'.2f'))
#Error statement and flag when invalid input is entered for membership status
        else:
            print('Invalid. Membership status should be y or n.')
            errorFlag = 88
#Error statement and flag when invalid input is entered for book quantity
    else:
        print('Invalid. Number should be between 1 and 3.')
        errorFlag = 88
        
#Decision making if customer chooses to buy Little Math Genius first
if choice == 'L':
#Prompting customer for quantity of books they would like to buy
    numberLittle = int(input('How many Little Math Genius books would you like to buy? (1 - 4) '))
#Condition to see if customer entered a valid number of books
    if numberLittle >= 1 and numberLittle <= 4:
#Prompting customer for membership status
        memberStatus = input('Are you a Learning Avenue Club member? (y - yes, n - no) ')
        if memberStatus == 'y':
#Cost calculation if customer is a member/receives member discount
            costLittle = numberLittle * LITTLEMATH * (1 - MEMBERDISCOUNT) * (1 + TAXRATE)
#Price output if customer is a member/receives member discount
            print('The charge is $',format(costLittle,'.2f'))
        elif memberStatus == 'n':
#Cost calculation if customer is not a member/receives no discounts
            costLittle = numberLittle * LITTLEMATH * (1 + TAXRATE)
#Price output if customer is not a member/receives no discounts
            print('The charge is $',format(costLittle,'.2f'))
#Error statement following invalid input for membership status
        else:
            print('Invalid. Membership status should be y or n.')
#Error statement following invalid input for book quantity
    else:
        print('Invalid. Number should be between 1 and 4.')

#Decision making if customer chooses to buy Little Math Genius after buying Greek Heroes using a flag 
if choice == 'G' and errorFlag != 88:
#Prompting customer if they would like to purchase Little Math Genius after buying Greek Heroes
    choiceLittleMath = input('Would you also like to buy Little Math Genius (y - yes, n - no)? ')
    if choiceLittleMath == 'y':
#Prompting customer for the quantity of books they would like to buy
        numberLittle = int(input('How many Little Math Genius books would you like to buy? (1 - 4) '))
#Condition to see if customer entered a valid number of books
        if numberLittle >= 1 and numberLittle <= 4:
            if memberStatus == 'y':
#Cost calculation if customer is a member/receives member discount
                costLittle = numberLittle * LITTLEMATH * (1 - MEMBERDISCOUNT) * (1 + TAXRATE)
#Price output if customer is a member
                print('The charge is $',format(costLittle,'.2f'))
#Calculating total cost of both book orders with member discount
                print('The total transaction cost is $',format(costLittle + costGreek,'.2f'))
            elif memberStatus == 'n':
#Cost calculation if customer is not a member/receives no discount
                costLittle = numberLittle * LITTLEMATH * (1 + TAXRATE)
#Price output if customer is not a member
                print('The charge is $',format(costLittle,'.2f'))
#Calculating total cost of both book order without member discount
                print('The total transaction cost is $',format(costLittle + costGreek,'.2f'))
#Error statement following invalid input for membership status
            else:
                print('Invalid. Membership status should be y or n.')
#Error statement following invalid input for book quantity
        else:
            print('Invalid. Number should be between 1 and 4.')
#Printed statement if customer decides to not buy Little Math Genius after buying Greek Heroes
    elif choiceLittleMath == 'n':
        print('Give the customer a 10% off coupon on Little Math Genius for the next transaction.')
#Error statement following invalid answer to whether or not customer wants to buy Little Math Genius
    else:
        print('Invalid. Choice to also buy Little Math Genius should be y or n.')

#Outputting end of program message
print()
print('End of program.')


