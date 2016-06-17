# SifExport for Python
# Version 0.1
# This script reads a predefined CSV file and exports it as SIF 
# We use this to import new students to our ILS
# There is also a PHP version available, this python version is at the moment more primitive

import csv
import datetime
import os

# Create a list from CSV
def ReadCSVasList(csv_file):
    try:
        with open(csv_file) as csvfile:
            reader = csv.reader(csvfile)
            datalist = []
            datalist = list(reader)
            return datalist
    except IOError as (errno, strerror):
            print("I/O error({0}): {1}".format(errno, strerror))
    return

#Read CSV to list
currentPath = os.getcwd()
csv_file = "export.csv"
csv_data_list = ReadCSVasList(csv_file)


#SIF needs a SYSDATE
t = datetime.date.today()
sysdate = t.strftime('%Y-%m-%d')


# Define a SIF file for export
f = open("sifExport.sif","w")

# Here we define the SIF. Read Voyager System manual for more information
# This could be defined better, but it works for now. 
for p in csv_data_list:
    surName = p[0]
    firstName = p[1]
    instid = p[2]
    streetAddress = p[3]
    zipCode = p[4]
    city = p[5]
    email = p[6]
    patronGroup = "LaY OPI"
    statCat = "E"
    purgeDate = "2021-05-15"

    patronID =""
    barcodeID =""
    barcode =""
    empty =""
    barcodeStatus="1"
    barcodeModified="2016.04.07"
    patronExpire="2382.12.31"
    voyagerDate=sysdate
    voyagerUpdated=sysdate

    nameType="1"
    middleName=""
    title=""
    addressCount="2"
    addressID=""
    
    addressType="1"
    addressStatus="N"
    addressBegin=sysdate
    addressEnd="2382.12.31"

    country=""
    phone="-"
    mobilephone="1234567"
    dateAdded=sysdate
    addressID2=""
    addressType2="3"
    addressBegin2=sysdate
    addressEnd2="2050.10.20"


# After all the data has been declared, let's write it into a file. No error checking at the moment. 

    f.write (patronID.rjust(10,'0'))
    f.write (barcodeID.rjust(10, ' '))
    f.write (barcode.ljust(25, ' '))
    f.write (patronGroup.ljust(10, ' '))
    f.write (barcodeStatus.ljust(1, ' '))
    f.write (barcodeModified.ljust(10, ' '))
    f.write (empty.ljust(122, ' ' ))
    f.write (patronExpire.ljust(10, ' '))
    f.write (purgeDate.ljust(10, " "))
    f.write (voyagerDate.ljust(10, " "))
    f.write (voyagerUpdated.ljust(10, ' '))
    f.write (empty.ljust(10, ' '))
    f.write (instid.ljust(30, ' '))
    f.write (empty.ljust(11, ' '))
    f.write (statCat.ljust(3, ' '))
    f.write (empty.ljust(27, ' '))
    f.write (nameType.ljust(1, ' '))
    f.write (surName.ljust(30, ' '))
    f.write (firstName.ljust(20, ' '))
    f.write (middleName.ljust(20, ' '))
    f.write (title.ljust(10, ' '))
    f.write (empty.ljust(65, '0'))
    f.write (addressCount)
    f.write (addressID.ljust(10, '0'))
    f.write (addressType)
    f.write (addressStatus)
    f.write (addressBegin.ljust(10, ' '))
    f.write (addressEnd.ljust(10, ' '))
    f.write (streetAddress.ljust(50, ' '))
    f.write (empty.ljust(160, ' '))
    f.write (city.ljust(40, ' '))
    f.write (empty.ljust(7, ' '))
    f.write (zipCode.ljust(10, ' '))
    f.write (country.ljust(20, ' '))
    f.write (phone.ljust(25, ' '))
    f.write (mobilephone.ljust(20, ' '))
    f.write (empty.ljust(50, ' '))
    f.write (dateAdded.ljust(10, ' '))
    f.write (addressID2.ljust(10, '0'))
    f.write (addressType2)
    f.write (addressStatus)
    f.write (addressBegin2.ljust(10, ' '))
    f.write (addressEnd2.ljust(10, ' '))
    f.write (email.ljust(50, ' '))
    f.write (empty.ljust(337, ' '))
    f.write (voyagerUpdated.ljust(10, ' '))
    f.write ('\n')





#print csv_data_list

# To Ignore 1st Row (Headers)
#csv_data_list.pop(0)
#print csv_data_list

# append to list
#csv_data_list.append(['6', 'Suresh', 'India'])

#print csv_data_list

