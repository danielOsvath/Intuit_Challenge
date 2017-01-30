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
import matplotlib.pyplot as plt

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



def avgSpending(user):
    """
        Get the average spending of a user, annually and monthly.

        :param user: user data instance.
    """

    sum = 0

    user[' Date'] = pandas.to_datetime(user[' Date'], format="%m/%d/%Y")

    start = "1/1/2013"
    end = "12/31/2014"

    years = user[(user[' Date'] >= pandas.to_datetime(start, format='%m/%d/%Y'))
    & (user[' Date'] <= pandas.to_datetime(end, format='%m/%d/%Y'))]

    amounts = years[' Amount'].values

    # transactionCount = amounts.shape[0]

    for cost in amounts:
        sum += abs(cost)


    monthly = (sum / AMOUNT_MONTHS)
    annually  = sum / 2

    return [monthly, annually]


# def recordData():
#     """
#         Assumes table headers already present in file results.csv
#     """


def main():
    """
        Read the data for a number of users, and record stats.
        (Assuming transaction data is provided, within range
        and named user-#.csv)

        :param amount: amount of user data to read
    """

    for current in range(0,1):

        currentUser = loadUserData(str(current))

        avgMonthly = avgSpending(currentUser)[0]
        avgAnnual = avgSpending(currentUser)[1]

        incomeEstimate = avgAnnual / 0.85

        #recordData(id,incomeEstimate,)




if __name__ == '__main__':
    main()