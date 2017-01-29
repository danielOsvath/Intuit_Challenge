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


def readUsers(amount):
    """
        Read the data for a number of users,
        assuming transaction data is provided, within range
        and named user-#.csv

        :param amount - amount of user data to read
    """

    for i in range(0,amount):
        filename = "transaction-data/user-" + str(i) + ".csv"
        loadUserData(filename)


def loadUserData(filename):
    """
        Load the data for a user.
    """
    user = pandas.read_csv(filename)
    print(user.columns)




def main():
    readUsers(5)

if __name__ == '__main__':
    main()