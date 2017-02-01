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

from prettytable import PrettyTable

#amount of user data to read.
NUMBER_OF_USERS = 100

#amount of data for each user.
AMOUNT_MONTHS = 24


def loadUserData(current):
    """
        Load the data for a user, specified by number.

        :param current: the number of the current user.

        :returns the user (pandas) file instance.
    """
    filename = "transaction-data/user-" + current + ".csv"
    user = pandas.read_csv(filename)

    return user


def avg_spending_and_income(year,user):
    """
        Get the average monthly, annual spending of a user, and income
        for the given year.

        :param  year: the given year
                user: user data instance.

        :returns an array of data [monthlyAvgExpense, annualExpense, income]
    """

    expensesum = 0
    income = 0

    # format dates from csv column
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


def spending_income(user):
    """
        Get the spending and income information for the two years of data.

        :param user: the user data instance.

        :returns an array of strings that notes the avg monthly spending and
        income for years 2013 and 2014. (String array bc. ready to write for csv)
    """

    spending_and_income_2013 = avg_spending_and_income("2013", user)

    avgMonthly_2013 = int(round(spending_and_income_2013[0],0))
    # annual_2013 = spending_and_income_2013[1]
    income_2013 = int(round(spending_and_income_2013[2],0))

    spending_and_income_2014 = avg_spending_and_income("2014", user)

    avgMonthly_2014 = int(round(spending_and_income_2014[0],0))
    # annual_2014 = spending_and_income_2014[1]
    income_2014 = int(round(spending_and_income_2014[2],0))

    yrOne = "Avg Monthly Sp.: $" + str(avgMonthly_2013) + \
            "\n Total Income : $" + str(income_2013) + "\n"
    yrTwo = "Avg Monthly Sp.: $" + str(avgMonthly_2014) + \
            "\n Total Income : $" + str(income_2014) +"\n"

    return [yrOne, yrTwo]


def containsKey(string, array):
    """
        Check whether an array of keywords contains a specific keyword.

        :param  string: keyword to look for
                array: array of keywords.

        :returns a boolean whether the array contains the keyword.
    """

    string = string.upper()

    for element in array:
        s = element.upper()
        if string in s: return True

    return False


def checkStudent(keywords):
    """
        Checks the keywords for course,
        (things that are associated with students) and returns
        a string for the csv table.

        :param keywords: array of keywords to search.

        :returns a string representing the result.
    """

    if containsKey("Course", keywords) or containsKey("Education",keywords):
        return "Yes"
    else:
        return "No"


def checkChildren(keywords):
    """
        Checks the keywords for things that are associated with children,
        or babies and returns a string for the csv table.

        :param keywords: array of keywords to search.

        :returns a string representing the result.
    """

    babyComing = containsKey("Prenatal", keywords)
    baby = containsKey("Baby", keywords)

    if babyComing:
        return "Baby is on the way."
    elif baby:
        return "Has children."
    else:
        return "No Children."


def checkRelationship(keywords):
    """
        Checks the keywords for things that are associated with relationships,
        and returns a string for the csv table.

        :param keywords: array of keywords to search.

        :returns a string representing the result.
    """

    divorce = containsKey("Divorce", keywords)
    jewelry = containsKey("Jewelry", keywords)
    wedding = containsKey("wedding", keywords)

    if divorce:
        return "Thinking about divorce."
    elif wedding:
        return ("Planning wedding.")
    elif jewelry:
        return "Recently purchased jewelry, relation seems to be healthy."
    else:
        return "No troubling signs."


def isTransportation(string):
    """
        Check if a certain string is associated with transportation expenses.

        :param string - string to check

        :returns boolean whether is associated with transport.
    """

    s = string.upper()

    transp = ["TAXI", "LYFT", "UBER", "TRANSPORT"]

    for m in transp:
        if m in s:
            return True

    return False


def stripkeyWords(str):
    """
        Strip common keywords from transactions, to be written as hobbies.

        :param str: string to strip

        :returns string as hobby label
    """

    notHobby = ["Food", "Apparel", "Courses", "Grill", "Restaurant", "Coffee",
                "Vitamin",]

    for n in notHobby:
        if n in str:
            str = ""
            return str

    replaceDict = { " Ticket" : "s", " Supplies" : "", " Course Fees" : "",
                    "Auction" : "Auctions", "Art's " : "",
                    "Amazon Order - " : "", "Delivery" : "", " Rental" : "",
                    " Membership" : "", " Fees" : "", " Book" : "",
                    "Library" : "Reading", "DVD - " : "", "GNC" : "Sports",
                    "Paining Course" : "Painting", "Paint Bushes" : "",
                    " Subscription" : "s", "Paint Canvas" : "",
                    "Game - PlayStation" : "Games", " Equipment" : "s",
                    " Course" : ""}

    for key in replaceDict:
        str = str.replace(key, replaceDict[key])

    return str


def checkHobbies(rankedkeywords):
    """
        Check for a user's hobbies.
        Takes into account the type of most frequent
        transactions within the two year period.

        A good number to check above is 80,
        meaning the transaction is repeated on the avg of every 9 days.

        :param rankedkeywords: the transaction keywords ranked by count

        :returns string of hobbies for the user.

    """
    hobbies = ""

    indexes = rankedkeywords.index  # need to do this way because of pandas lib.

    for keyW in indexes:
        if rankedkeywords[keyW] >= 80 and not isTransportation(keyW):

            s = stripkeyWords(keyW)
            if s != "":
                hobbies += s + ". "

    return hobbies


def checkOther(keywords):
    """
        Check additional info for the user.

        :param keywords: keywords from transactions.

        :returns other info about user.
    """

    otherInfo = ""

    otherDict = { "Move" : "Moving from home soon. ",
                  "Overdraft Fee" : "Had overdraft fees. ",
                  "Hotel" : "Has Traveled. "}

    for key in otherDict:
        if containsKey(key, keywords):
            otherInfo += otherDict[key]

    return otherInfo


def getUserFeatures(currentUser):
    """
        Checks the keywords for things that are associated with user features,
        and returns a row of data (arr of str) for the csv table.

        :param currentUser: data instance of the current user.

        :returns an array of strings redy to be written in a csv table.
    """

    userData = []

    # Get transactions by frequency.
    rankedKeywords = currentUser[' Vendor'].value_counts()

    # Types of transactions.
    keywords = rankedKeywords.index.tolist()

    userData.append(currentUser['auth_id'].iloc[0])

    # Check keywords for features and append result to userData array.
    userData.append(checkStudent(keywords))
    userData.append(checkChildren(keywords))
    userData.append(checkRelationship(keywords))
    userData.append(checkHobbies(rankedKeywords))
    userData += spending_income(currentUser)  # returns arr. -> +=
    userData.append(checkOther(keywords))

    return userData


def createCSV(header):
    """
        Create the default csv, and print header row for table.
    """
    c = csv.writer(open("results.csv", "w"))

    c.writerow(header)

    return c


def loadInfo():

    print("RIT Intuit Challenge by Daniel Osvath Londono \n"
          "Writing csv file to project directory and creating table...")


def main():
    """
        Read the data for a number of users, and record info in results table.
        (Assuming transaction data is provided, within range
        and named user-#.csv)
    """

    loadInfo()

    header = ["User ID", " Student ", " Children ", " Relationship Info ",
              " Hobbies ", " 2014 Financials ", "2013 Financials ", " Other "]

    table = PrettyTable(header) # create table for output.
    c = createCSV(header)  # create the results file.

    for current in range(0,NUMBER_OF_USERS):

        currentUser = loadUserData(str(current))

        # get feature data for current user
        userData = getUserFeatures(currentUser)

        c.writerow(userData)
        table.add_row(userData)

    print(table)


if __name__ == '__main__':
    main()