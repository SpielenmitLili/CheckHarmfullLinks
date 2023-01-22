#
#  _     _ _ _               _
# | |   (_) (_)___ _   _ ___| |_ ___ _ __ ___
# | |   | | | / __| | | / __| __/ _ \ '_ ` _ \
# | |___| | | \__ \ |_| \__ \ ||  __/ | | | | |
# |_____|_|_|_|___/\__, |___/\__\___|_| |_| |_|
#                  |___/
#
# This program was created with ❤️ by Lili Chelsea Urban in Saarburg (Germany)
# Contact: https://spielenmitlili.com/kontakt
#
#

# Check if links in a list are already blocked by rpi-list

# Import needed modules
import datetime
import socket
import time
import getpass

# Define all needed variables
allRecords = 0
notFoundRecords = 0
foundRecords = 0

# Get current time
currentTime = datetime.datetime.now()
date_time = currentTime.strftime("%m/%d/%Y, %H:%M:%S")

# Start program with header
print("#############################################################################")
print(date_time + " | Process successfuly started for user " + getpass.getuser() + " on " + socket.gethostname() + " in program CheckHarmfullLinks")
print(date_time + " | CheckHarmfullLinks by Lili Chelsea Urban started!")
print("#############################################################################")
print(" ")
print(" ")
print(" ")

# Open file with potencially harmful links
with open("harmfullList.txt") as file:
    # Each link needs to be checked once
    for line in file:

        # Prepare line to work
        line = line.rstrip()
        print(line)

        # Check if line is empty
        if line != "":
            # Try to resolve given domain
            try:
                DNS_record = socket.gethostbyname(line)

                # If domain successfully resolved write answer to console
                print(DNS_record)

                # Check for false-positives
                if DNS_record != "0.0.0.0" and DNS_record != "::":
                    # If not a false positive, then write domain to file
                    f = open("results.txt", "a")
                    f.write(line + "\n")
                    f.close()

                    # Print result to console
                    print("DNS-Record wurde in die Datei übernommen!")

                    # Add +1 to variable
                    foundRecords += 1
                else:
                    # If false positive only write short info to console
                    print("Der oben angegebene Record konnte nicht aufgelöst werden!")

                    # Add +1 to Variable
                    notFoundRecords += 1
            except:
                # If domain don't exist skip and only write some short info into console
                print("Der oben angegebene Record konnte nicht aufgelöst werden!")

                # Add +1 to Variable
                notFoundRecords += 1

            # Sleep for a second so DNS-Server don't block script for spam
            time.sleep(1)

            # Add +1 to Variable
            allRecords += 1

# Sort all records in file alphabetically

# Define list for all records in the file
toSort = []

# Get domains from file to array
with open ("results.txt", "r") as f:
    for line in f:
        stripped = line.strip("\n")
        toSort.append(stripped)

# Sort array
toSort = list(dict.fromkeys(toSort))
toSort.sort()

# Write sorted result to new file
with open ("results_sorted.txt", "w") as file:
    for k in toSort:
        file.write(k + "\n")

# Get current time
currentTime = datetime.datetime.now()
date_time = currentTime.strftime("%m/%d/%Y, %H:%M:%S")

# Write all records at the end to console
print(" ")
print(" ")
print(" ")
print("#############################################################################")
print(date_time + " | CheckHarmfullLinks by Lili Chelsea Urban ended!")
print("#############################################################################")
print(" ")
print(" ")
print(" ")

print("#############################################################################")
print("RESULTS:")
print("All links checked: " + allRecords)
print("Already blocked links found: " + notFoundRecords)
print("Not blocked links found: " + foundRecords)
print("#############################################################################")

print(" ")
print(" ")
print(" ")

print(date_time + " | Process successfuly completed for user " + getpass.getuser() + " on " + socket.gethostname() + " in program CheckHarmfullLinks")

#
# Copyright 2022 by Lili Chelsea Urban. All Rights Reserved
#
