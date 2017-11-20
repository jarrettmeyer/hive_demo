import datetime
import random
import sys

# Ensure that a max lines argument was given.
if len(sys.argv) < 2:
    print "Usage python ./create_weather_ext.py <year>"
    exit(-1)

# Get year and month values from input arguments.
year = int(sys.argv[1])

# Change this if you want. It's only for demo purposes. :)
city = "Indianapolis"
state = "IN"

temp = 20.0
ts = datetime.datetime(year, 1, 1, 0, 0, 0)

while ts.year == year:
    month = ts.month
    path_to_file = "../demo_files/weather_ext_%d_%d.txt" % (year, month)
    print "Creating sample file for %d-%d" % (month, year)
    file_ptr = open(path_to_file, "w")
    while ts.month == month:
        # Compute the new temperature reading using a random walk.
        diff = random.random() * 0.5 - 0.25
        temp = temp + diff
        # Write the temperature reading to the text file.
        file_ptr.write("%s,%s,%s,%.1f\n" % (ts, city, state, temp))
        ts = ts + datetime.timedelta(0, 60) # Add 60 seconds.
    file_ptr.close()


print "Done.\n"
