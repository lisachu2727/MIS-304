#Name: Tzu-Chuan Chu
#Assignment Number: 7
#Date: 11/16/18
#Section 8:00-9:30
#Description: This program is made is made of a class and application programs.
#Description: The application uses the class to create cookie objects. This program can
#Description: display cookie information, change the price of a cookie, and show cookie
#Description: inventory.

#Importing cookie file
import cookie

#Defining main() function
def main():
    
    #Instantiating cookies
    chocolateChip = cookie.Cookie('chocolate chip', 10, 4.50)
    strawberry = cookie.Cookie('strawberry', 30, 3.00)
    sugar = cookie.Cookie('sugar', 15, 2.50)

    #Creating empty list 
    cookieList = []

    #Adding the three cookies into empty list
    cookieList.append(chocolateChip)
    cookieList.append(strawberry)
    cookieList.append(sugar)

    #Initializing for while loop
    menuChoice = 'a'

    #Looping menu choices
    while menuChoice != 'e':
        try:
            #Calling display menu function
            menuChoice = displayMenu().lower()

            #Decision making for menu choice 'a'
            if menuChoice == 'a':
                #Calling printAllCookies() function
                printAllCookies(cookieList)

            #Decision making for menu choice 'b'
            elif menuChoice == 'b':
                #Prompting for cookie type and price
                cookieType = input('Please enter the cookie type: ').lower()
                cookiePrice = float(input('Please enter the new price of the cookie: '))
                print()
                #Calling setPrice() function
                newPrice = setPrice(cookieList,cookieType, cookiePrice)

                #Decision making if cookie type is not found
                if newPrice == 0:
                    print('Cookie type not found.')
                    print()

            #Decision making for menu choice 'c'
            elif menuChoice == 'c':
                #Prompting for cookie type
                cookieType = input('Please enter the cookie type: ').lower()
                #Calling outputCookieInventory() function
                inventory = outputCookieInventory(cookieList, cookieType)
                #Decision making if cookie type is not found
                if inventory == 0:
                    print('Cookie type not found.')
                    print()
                else:
                    print('The inventory is ',inventory)
                    print()

                
                    
        except ValueError:
            print('Value error.')
            print()
        except Exception as err:
            print(err)
            print()
            
#Defining displayMenu() function
def displayMenu():
    #Printing out menu title
    print('Welcome to Best Cookies!')
    print('=========================')
    #Printing out menu choices
    print('a: Output information for all cookies')
    print('b: Set a new price for one cookie')
    print('c: Output inventory for a specific cookie')
    print('e: Exit the program')
    #Printing empty line
    print()

    #Prompting for menu choice
    menuChoice = input('Please enter your choice: ').lower()
    #Printing empty line
    print()

    #Validation loop for valid menu choice
    while menuChoice != 'a' and menuChoice != 'b' and \
    menuChoice != 'c' and menuChoice != 'e':
        menuChoice = input('Invalid choice. Please try again: ').lower()
        print()

    #Returning menu choice back to main() function
    return menuChoice 

#Defining printAllCookies() function
def printAllCookies(cookieList):
    #Loop to print out each cookie in list
    for cookie in cookieList:
        print(cookie)
        print()

#Defining setPrice() function
def setPrice(cookieList, cookieType, price):
    flag = 0
    #Loop to search for cookie type
    for cookie in cookieList:
        #Decision making if cookie type found
        if cookie.get_cookieType() == cookieType: 
            cookie.set_price(price)
            flag = 1
            #Breaking out of loop
            break
    #Returning flag value
    return flag

#Defining outputCookieInventory() function
def outputCookieInventory(cookieList, cookieType):
    flag = 0
    #Loop to search for cookie type
    for cookie in cookieList:
        #Decision making if cookie type found
        if cookie.get_cookieType() == cookieType:
            flag = cookie.get_inventory()
            break
        #Decision making if cookie type is not found
    return flag


#Calling main() function 
main()
