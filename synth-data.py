# Create a random data set and writes to a file.
# Author: Drew Heasman
# Date: December 19, 2018
# Future implimentation:    Explode high value instances of uranium along elongated, "fault-like" directions.
#                           Add a sandstone/basement value (binary) (possibly just a set value with no randomness
#                           Add illite plumes to sandstone.
#                           Create fault like areas with no uranium values (perhaps a graphite value)

import random

U = []          #initialize the random data list.
uran = 0        #initialize the uranium value

for x in range(0, 100):                                 #loop to create a random data set with x,y, and z coord
    for y in range(0, 100):
        for z in range(0, 100):
            uran = random.randint(-1500000, 50000)      #set the statistical variance of high value uranium
            if uran < 100:                              #set the base limit of uranium values
                uran = 100
            U.append([x, y, z, uran])                   #append the uranium value to the x, y, z, coord in the list

with open('test_data.csv', 'w') as f:                   #write the entire list to a file
    for item in U:
        f.write("%s\n" % item)
