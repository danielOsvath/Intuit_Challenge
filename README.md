# Intuit_Challenge

## Install 

### 1) Download project from Github as a .zip. 
(I have invited Intuit-Recruiting on Github as a collaborator.)

https://github.com/danielOsvath/Intuit_Challenge/invitations

**Important:** Please use transaction .csv files from the downloaded .zip from my project, because the original ones for the challenge had a mistake: there were dates 12/32/2013 and 12/32/2014, which caused errors for date formatting libraries, as there is no 32nd day in a month. This has been fixed in the files of my project.

### 2) Download Anaconda – a library for data tools

https://www.continuum.io/downloads#osx

Download the graphical or command line installer and install, there are specific instructions through the above link when you scroll down. 

## Running (Mac) 

Open **terminal.** 

Before running, make sure the terminal window is at least 350 characters in width, because it outputs a wide table (you may have to do some dragging). **350 x 62** is a good size. 

Type: `python`

If you see:
Python 3.5.2 |Anaconda 4.2.0 (x86_64)| , and the anaconda label is there, you are set to run the project by browsing to the project folder 

and typing: `python readData.py`

If the anaconda label is **not** there, you will have to provide the anaconda python path. Usually in the following location: ~/anaconda/bin/python.app 

To run: `~/anaconda/bin/python.app readData.py` 

or: `~/anaconda3/bin/python.app readData.py`

When in the project directory. 

In addition to the displayed table, the program will output a .csv in the project folder.




## Rationale behind data analysis

### Student
To determine whether the user is a student for the purposes of this assignment, the program simply looks for the keywords *Course* or *Courses* in the transaction data. Any individual taking a course i.e. learning something is considered a student. It need not be a college enrolled student. 

### Children
There were two prevalent key features in the user transaction data that suggest the user may have or be expecting a child. The first is *Prenatal Care*, which suggest the user is bound to have a child. Second, *Baby*, if the keyword is present in transaction data then, for this assignment, we can infer that the user has a child. Finally, if none of these keywords are present, we may assume the user has no children. 

### Relationship Info
There were three prevalent key features in the user transaction data that can reveal information about a user’s relationship. First: *Divorce*, we may assume that users who have paid a divorce attorney are thinking about divorce. Second: *Wedding*, we may assume that users who have paid a wedding planner are thinking about a wedding. (It is assumed only one of these cases is true, one can not be planning a divorce if not married, nor planning a wedding if already thinking about divorce). Third: *Jewelry*, if the keywords wedding and divorce are not triggered, then through jewelry we can assume the relationship is healthy. If none of these are found, we assume there are no troubling signs for the relationship. 
