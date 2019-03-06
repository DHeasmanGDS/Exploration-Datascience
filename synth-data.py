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

with open('test_data.csv', 'w') as f:                   #write the entire list to a file
    for item in U:
        f.write("%s\n" % item)
