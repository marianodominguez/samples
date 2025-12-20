#!/usr/bin/env python

from datetime import datetime

# Get the current time
t1=datetime.now()
print(t1)

# Parse a time string
t1 = datetime.strptime("17:45:52,186", "%H:%M:%S,%f")
print(t1)

# Format for datetime constructor
#datetime(year, month, day[, hour[, minute[, second[, microsecond[, tzinfo]]]]])
