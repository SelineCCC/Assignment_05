#------------------------------------------#
# Title: CDInventory.py
# Desc: Store CD Inventory data using dictionaries in 2D structure
# Change Log: (Who, When, What)
# JingyinChen, 2021-Aug-08, Created File
#------------------------------------------#

# Declare variables 

strChoice = '' # User input
lstTbl = []  # list of lists to hold data
dicTbl = {}  # dictionaries to be displayed from file data
dicRow = {}  # dictionaries to be hold in lists
lstRow = []  # list of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# Get user Input 
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('[l] load Inventory from file (Please only load it once each time)')
    print('[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory (Please only delete the entry you entered this time)')
    print('[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()
    if strChoice == 'x':
        # 5. Exit the program if the user chooses so
        break
    if strChoice == 'l':
        # Add the functionality of loading existing data
        objFile = open(strFileName, 'r')
        for row in objFile:
            lstRow = row.strip().split(',')
            dicTbl = {'id': lstRow[0], 'title': lstRow[1], 'artist': lstRow[2]}
            lstTbl.append(dicTbl)
        objFile.close()
        for row in lstTbl:
            print(row.values())
        print('\n\n')
    elif strChoice == 'a':
        # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # 2. Add data to the table (2d-list) each time the user wants to add data
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID)
        dicRow = {'id': intID, 'title': strTitle, 'artist': strArtist}
        lstTbl.append(dicRow)
        print('\n\n')
    elif strChoice == 'i':
        # 3. Display the current data to the user each time the user wants to display the data
        print('ID, CD Title, Artist')
        for row in lstTbl:
            print(*row.values(), sep = ', ')
        print('\n\n')
    elif strChoice == 'd':
        # Add functionality of deleting an entry
        print('Current data are(is):' + str(lstTbl))
        intIDDelete = input('Please enter the ID of the entry you want to delete: ')
        strTitleDelete = input('Please enter the CD Title of the entry you want to delete: ')
        strArtistDelete = input('Please enter the CD Title of the entry you want to delete: ')
        dicDelete = {'id': int(intIDDelete), 'title': strTitleDelete, 'artist': strArtistDelete}
        lstTbl.remove(dicDelete)
        print('Data after deleting are(is):' + str(lstTbl))
        print('\n\n')
    elif strChoice == 's':
        # 4. Save the data to a text file CDInventory.txt if the user chooses so
        objFile = open(strFileName, 'w')
        for row in lstTbl:
            strRow = ''
            for item in row.values():
                strRow += str(item) + ','
            strRow = strRow[:-1] + '\n'
            objFile.write(strRow)
        objFile.close()
        print('\n\n')
    else:
        print('Please choose either l, a, i, d, s or x!')

