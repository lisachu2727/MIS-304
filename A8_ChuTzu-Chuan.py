#Name: Tzu-Chuan Chu
#Assignment Number: 8
#Date: 11/27/18
#Section: 8:00-9:30
#Description: This is an object oriented based program. This program allows
#Description: the user to see dress information and change the price of a dress
#Description: among multiple dresses in a list.

#Importing dress file
import dress

#Defining main function
def main():

    #Instantiating new dresses and preowned dresses
    dressOne = dress.Dress('D111', 'Floral', 'Jenny Flower', 'Medium', 695.98)
    dressTwo = dress.Dress('D112', 'Maxi', 'John Dalsey', 'Small', 199.98)
    dressThree = dress.PreOwnedDress('D113', 'Wrap', 'Jason Georges', \
                                     'Medium', 111.88, 2016)
    dressFour = dress.PreOwnedDress('D114', 'Floral', 'Jenny Flower', \
                                    'Large', 100.85, 2015)

    #Creating empty list for dresses
    dress_list = []

    #Appending the four dresses into the empty list
    dress_list.append(dressOne)
    dress_list.append(dressTwo)
    dress_list.append(dressThree)
    dress_list.append(dressFour)

    #Initializing while loop
    repeat = 'yes'

    #Looping menu
    while repeat == 'yes':

        #Outputting menu
        print('Welcome to the dress program!')
        print('==============================')
        print('A - Print dress information of a designer')
        print('B - Change the price of a dress')
        print()

        #Prompting initial menu choice
        choice = input('Please enter menu choice (A or B): ').lower()

        #Looping menu choices
        while choice != 'a' and choice != 'b':

            #Prompting menu choice
            choice = input('Invalid. Please re-enter your choice: ').lower()     

        #Menu choice A
        if choice == 'a':
            #Prompting designer name
            designer = input("Please enter the designer's name: ")
            #Calling PrintDressByDesigner function
            PrintDressByDesigner(dress_list, designer)

        #Menu choice B
        elif choice == 'b':
            #Calling ChangePrice function
            ChangePrice(dress_list)     

        #Prompting for repeating loop
        repeat = input('Do you want to continue the program? (yes or YES): ').lower()         

#Defining PrintDressByDesigner function
def PrintDressByDesigner(dressList, designer):
    #Loop to search for dress by designer
    for dress in dressList:
        if dress.get_designer() == designer:
            #Outputting dress information
            print(dress)

#Defining ChangePrice function
def ChangePrice(dressList):
    #Initializing flag
    flag = 0

    #Prompting for dress ID and desired price
    dressID = input('Please enter the dress ID: ')
    newPrice = float(input('Please enter the new price: '))
    print()

    #Validation loop for checking the entered price
    while newPrice <= 0 or newPrice >= 2000:
        print('The new price must be between $0 and $2000.00.')
        newPrice = float(input('Please re-enter the new price: '))

    #Loop to search for dress based on ID
    for dress in dressList:
        if dress.get_dress_id() == dressID:
            dress.set_price(newPrice)
            #Flag set if dress is found
            flag = 1

    #Checking to see whether or not dress is found
    if flag == 1:
        print('The price is updated.')
    else:
        print('Dress not found. Price not updated.')

#Calling main function   
main()
