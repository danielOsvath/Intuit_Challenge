"""
    Main file for the RIT intuit challenge.
    Parses the data and creates a new table that includes a
    wide range of distinct details (or features)
    about each individual from the data set.
    file: readData.py
    author: Daniel Osvath Londono
    created Jan 29 2017
"""

import pandas
import csv

#amount of user data to read.
NUMBER_OF_USERS = 100

#amount of data for each user.
AMOUNT_MONTHS = 24



def loadUserData(current):
    """
        Load the data for a user.
    """
    filename = "transaction-data/user-" + current + ".csv"
    user = pandas.read_csv(filename)

    return user



def avg_spending_and_income(year,user):
    """
        Get the average monthly, annual spending of a user, and income
        for the given year.

        :param user: user data instance.
    """

    expensesum = 0
    income = 0

    user[' Date'] = pandas.to_datetime(user[' Date'], format="%m/%d/%Y")

    start = "1/1/" + year
    end = "12/31/" + year

    years = user[(user[' Date'] >= pandas.to_datetime(start, format='%m/%d/%Y'))
    & (user[' Date'] <= pandas.to_datetime(end, format='%m/%d/%Y'))]

    amounts = years[' Amount'].values

    # transactionCount = amounts.shape[0]

    for amount in amounts:
        if (amount < 0):
            expensesum += abs(amount)
        else:
            income += amount

    monthlyAvg = (expensesum / 12)
    annually = expensesum

    return [monthlyAvg, annually, income]


def spending_income(user,userData):

    spending_and_income_2013 = avg_spending_and_income("2013", user)

    avgMonthly_2013 = spending_and_income_2013[0]
    annual_2013 = spending_and_income_2013[1]
    income_2013 = spending_and_income_2013[2]

    spending_and_income_2014 = avg_spending_and_income("2014", user)

    avgMonthly_2014 = spending_and_income_2014[0]
    annual_2014 = spending_and_income_2014[1]
    income_2014 = spending_and_income_2014[2]

    yrOne = "Avg monthly spending: " + str(avgMonthly_2013) + " Income : " + str(income_2013)
    yrTwo = "Avg monthly spending: " + str(avgMonthly_2014) + " Income : " + str(income_2014)

    userData += [yrOne, yrTwo]


def containsKey(string, array):
    """
        Boolean.
    """
    string = string.upper()

    for element in array:
        s = element.upper()
        if (string in s): return True

    return False


def checkStudent(keywords, userData):

    if (containsKey("Course", keywords)):
        userData.append("Yes")
    else:
        userData.append("No")


def checkChildren(keywords,userData):

    babyComing = containsKey("Prenatal", keywords)
    baby = containsKey("Baby", keywords)

    if(babyComing):
        userData.append("Baby is on the way.")
    elif(baby):
        userData.append("Has children")
    else:
        userData.append("No Children")


def checkRelationship(keywords, userData):

    divorce = containsKey("Divorce", keywords)
    jewelry = containsKey("Jewelry", keywords)
    wedding = containsKey("wedding", keywords)

    if(divorce):
        userData.append("Thinking about divorce.")
    elif(wedding):
        userData.append("Planning wedding.")
    elif(jewelry):
        userData.append("Recently purchased jewelry, relation seems to be healthy.")
    else:
        userData.append("No troubling signs.")


def createCSV():
    """
        Create the default csv.
    """
    c = csv.writer(open("results.csv", "w"))

    c.writerow(["User ID", " Student ", " Children ", " Relationship Info ",
                " Hobbies ", " 2014 Financials ", "2013 Financials ", " Other "])

    return c

def main():
    """
        Read the data for a number of users, and record info in results table.
        (Assuming transaction data is provided, within range
        and named user-#.csv)

        :param amount: amount of user data to read
    """

    c = createCSV()  # create the results file.

    for current in range(0,100):

        userData = [] # data of current user

        currentUser = loadUserData(str(current))

        # get top counts - return array of strings of top transactions
        rankedKeywords = currentUser[' Vendor'].value_counts()
        keywords = rankedKeywords.index.tolist()

        userData.append(currentUser['auth_id'].iloc[0])

        checkStudent(keywords,userData)

        checkChildren(keywords,userData)

        checkRelationship(keywords,userData)

        c.writerow(userData)

        #spending_and_income = spending_income(currentUser,userData)

        #lloking to move:
        moving = (containsKey("Move",keywords) or containsKey("Movers",keywords))

        #Troubling paycheck finances,
        # could be getting larger paycheck if income < 1/2 * expense ->
        # trouble for relationship

        #hobbies

        print(userData)



if __name__ == '__main__':
    main()