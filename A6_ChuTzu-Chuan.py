#Name: Tzu-Chuan Chu
#Assignment Number: 6
#Date: 11/1/19
#Section 8:00-9:30
#Description: This is a program made for Mrs. String to perform some simple operations on a
#Description: string. This program can determine of the string is only made out of letters,
#Description: count the number of words in the string, and convert to string to fully
#Description: uppercase.

#Defining function main()
def main():
    #Creating string variable
    string = 'Python is one of the most popular programming languages in 2018. So is Java.'

    #Initializing variable to start loop
    redoChoice = 'yes'

    #Creating loop for string operations
    while redoChoice == 'yes' or redoChoice == 'YES':

        #Printing out menu
        print('Welcome to the string program')
        print('===============================')
        print('A or a: Output the string information to the screen')
        print('B or b: Count the number of words in a string.')
        print('C or c: Convert text to uppercase.')
        print()

        #Prompting for operation choice
        operationChoice = input('Please enter your choice: ')
        print()

        #Decision for outputting string information
        if operationChoice == 'A' or operationChoice == 'a':
            #Calling function printStringInfo()
            printStringInfo(string)

        #Decision for counting number of words in string
        elif operationChoice == 'B' or operationChoice == 'b':
            #Receiving and printing out number of words from function countWords()
            length = countWords(string)
            print('The string has',length,'words.')

        #Decision for converting string to all uppercase
        elif operationChoice == 'C' or operationChoice == 'c':
            print('The converted string is:\n',string.upper(),sep='')

        else:
            print('Invalid choice.')
        print()

        #Prompting for another string operation
        redoChoice = input('Do you want to perform another string operation? ')
        print()

#Declaring function printStringInfo()         
def printStringInfo(string):
    #Printing out string
    print(string)

    #Decision if string is made out of only letters
    if string.isalpha():
        print('This string only contains letters.')
    #Decision if string is not only made out of letters
    else:
        print('This string does not only have letters.')

    print()

#Declaring function countWords()
def countWords(string):
    #Spliting string
    length = len(string.split())
    #Taking length of string list and returning value into function main()
    return length

#Calling function main()
main()
