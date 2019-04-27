#Name: Tzu-Chuan Chu
#Assignment Number: 5
#Date: 10/26/18
#Section: 8:00-9:30
#Description: This program reads employee ID and wage information in a text file
#Description: and then processes the highest monthly salary for each employee as well as
#Description: each employee's average monthly salary. This program also calculates the
#Description: average salary for each month.

#Defining function main()
def main():
    #Declaring constants
    NUMBERMONTHS = 4
    
    #Initializing totals for each month
    totalJune = 0
    totalJuly = 0
    totalAugust = 0
    totalSeptember = 0

    #Initializaing number of employees
    numberEmployees = 0

    #Initializing division by zero flag
    zeroFlag = 0
    
    #Opening wages file
    wageData = open('H5_Wages.txt', 'r')
    
    #Reading line of employee ID in wages file
    employee = wageData.readline().rstrip('\n')

    try:
        while employee != '':
            #Declaring empty list
            wageList = []

            #Appending employee ID to list
            wageList.append(employee)
        
            #Reading and appending wages from June to list
            juneWages = float(wageData.readline())
            #Adding wage to June's total wages
            totalJune = totalJune + juneWages
            wageList.append(juneWages)
        
            #Reading and appending wages from July to list
            julyWages = float(wageData.readline())
            #Adding wage to July's total wages
            totalJuly = totalJuly + julyWages
            wageList.append(julyWages)
        
            #Reading and appending wages from August to list
            augustWages = float(wageData.readline())
            #Adding wage to August's total wages
            totalAugust = totalAugust + augustWages
            wageList.append(augustWages)
        
            #Reading and appending wages from September to list
            septemberWages = float(wageData.readline())
            #Adding wage to September's total wages
            totalSeptember = totalSeptember + septemberWages
            wageList.append(septemberWages)

            #Counter for number of employees
            numberEmployees = numberEmployees + 1

            #Receiving function calculatingAverage()
            employeeAverage = calculatingAverage(wageList,NUMBERMONTHS)

            #Slicing list to use max function
            wages = wageList[1:]
            maxWage = max(wages)

            #Printing out ID and monthly wages for each employee
            print('Employee ID: ',employee)
            print('June: ',format(juneWages,'.2f'))
            print('July: ',format(julyWages,'.2f'))
            print('August: ',format(augustWages,'.2f'))
            print('September: ',format(septemberWages,'.2f'))

            #Printing out calculations of wages for each employee
            print('The highest monthly salary is: ',format(maxWage,'.2f'))
            print('Average monthly salary for',employee,'is: ',format(employeeAverage,'.2f'))
            print()

            #Reading employee ID again
            employee = wageData.readline().rstrip('\n')

        #Calculating total monthly averages
        juneAverage = calculateAllAverages(totalJune,numberEmployees)
        julyAverage = calculateAllAverages(totalJuly,numberEmployees)
        augustAverage = calculateAllAverages(totalAugust,numberEmployees)
        septemberAverage = calculateAllAverages(totalSeptember,numberEmployees)

        #Printing out average wage report for each month
        print('Average Report for June, July, August, and September')
        print('======================================================')
        print('Average for June:\t',format(juneAverage,'.2f'))
        print('Average for July:\t',format(julyAverage,'.2f'))
        print('Average for August:\t',format(augustAverage,'.2f'))
        print('Average for September:\t',format(septemberAverage,'.2f'))
            
        #Closing wages file
        wageData.close()

    #Handling IOError
    except IOError:
        print('An error occured trying to read the file.')

    #Handling all other errors        
    except Exception as err:
        print(err)

#Defining function calculatingAverage
def calculatingAverage(nameList,months):
    #Initializing total wage
    total = 0
    #Slicing list to remove ID
    monthlyWage = nameList[1:]
    #Decision making to avoid division by zero
    if months < 1:
        print('Invalid. Number of months is less than 1.')
        #Activating flag for division by zero
        zeroFlag = -1
    else:
        #Accumulating total wages
        for wages in monthlyWage:
            total = total + wages
    #Calculating average monthly salary
    average = total / len(monthlyWage)
    
    return average

#Defining function calculateAllAverages
def calculateAllAverages(monthTotal,employeeTotal):
    #Calculating monthly average across all employees
    average = monthTotal / employeeTotal
    
    return average

#Calling function main()
main()
