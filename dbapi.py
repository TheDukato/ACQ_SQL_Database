import sys
import pymysql
import matplotlib.pyplot as plt

f = open("conf.txt", "r")
strin = f.readlines()

db = pymysql.connect(host=strin[0][0:-1],user=strin[1][0:-1],password=strin[2][0:-1])
cursor = db.cursor()

cursor.execute("use ACQ")
cursor.fetchone()

#DEBUG
cursor.execute("select Value,timeOfProbe from ACQ.historian where ID_Location = 1 AND timeOfProbe > '2022-10-01' AND timeOfProbe < '2022-10-03' ORDER BY timeOfProbe desc ")
data = cursor.fetchall()
print('Connection established '+ str(data[1]) )
#DEBUG

programArgs = sys.argv 
choosed_option = 0
at_index = 0

for x in range(len(programArgs)):
    if (programArgs[x] == "--add"):
        choosed_option = 1
        at_index = x
        break
    if (programArgs[x] == "--show"):
        choosed_option = 2
        at_index = x
        break
    if (programArgs[x] == "--delete"):
        choosed_option = 3
        at_index = x
        break
    if (programArgs[x] == "--modify"):
        choosed_option = 4
        at_index = x
        break       

print(programArgs[1:])

#ID_Loc = input("Enter ID_Location: ")

#cursor.execute("select Value,timeOfProbe from ACQ.historian where ID_Location = "+ID_Loc+" AND timeOfProbe > '2022-10-01' AND timeOfProbe < '2022-10-03' ORDER BY timeOfProbe desc ")
#data = cursor.fetchall()
