#!/usr/bin/env python

from datetime import datetime
t1=datetime.now()
print(t1)
t1 = datetime.strptime("17:45:52,186", "%H:%M:%S,%f")
print(t1)

#datetime(year, month, day[, hour[, minute[, second[, microsecond[, tzinfo]]]]])
