"""Human readable duration format

from Codewars
URL: https://www.codewars.com/kata/human-readable-duration-format

Your task in order to complete this Kata is to write a function 
which formats a duration, 
given as a number of seconds, in a human-friendly way.

The function must accept a non-negative integer. 
If it is zero, it just returns "now". 
Otherwise, the duration is expressed as a combination of 
years, days, hours, minutes and seconds.

(examples)
format_duration(62)    
    # returns "1 minute and 2 seconds"
format_duration(3662)  
    # returns "1 hour, 1 minute and 2 seconds"

For the purpose of this Kata, a year is 365 days and a day is 24 hours.

Note that spaces are important.

The resulting expression is made of components like 4 seconds, 1 year, etc. 
In general, a positive integer and one of the valid units of time, 
separated by a space. 
The unit of time is used in plural if the integer is greater than 1.

The components are separated by a comma and a space (", "). 
Except the last component, which is separated by " and ", 
just like it would be written in English.

A more significant units of time will occur before than 
a least significant one. 
Therefore, 1 second and 1 year is not correct, but 1 year and 1 second is.

Different components have different unit of times. 
So there is not repeated units like in 5 seconds and 1 second.

A component will not appear at all if its value happens to be zero. 
Hence, 1 minute and 0 seconds is not valid, but it should be just 1 minute.

A unit of time must be used "as much as possible". 
It means that the function should not return 61 seconds, 
but 1 minute and 1 second instead. Formally, 
the duration specified by of a component must not be greater than 
any valid more significant unit of time.
"""
# Test Function
def assert_equals(a, b):
    if a == b:
        print(True)
    else:
        print(False)

def format_duration(seconds):
    units = ["year", "day", "hour", "minute", "second"]
    secs_per_unit = [31536000, 86400, 3600, 60, 1]
    durations = [0] * len(units)
    ret = ""

    if seconds == 0:
        return "now"
    for i in range(len(units)):
        if seconds // secs_per_unit[i] >= 1:
            q, seconds = divmod(seconds, secs_per_unit[i])
            durations[i] = q
    for j in range(len(durations)):
        if durations[j]:
            if ret:
                ret += ", "
            unit = units[j] if durations[j] == 1 else units[j] + "s"
            ret += str(durations[j]) + " " + unit
    tmp = ret.split(",")
    if len(tmp) > 1:
        ret = ",".join(tmp[:-1])
        ret += " and" + tmp[-1]
    return ret

    
# Test Cases
assert_equals(format_duration(1), "1 second")
assert_equals(format_duration(62), "1 minute and 2 seconds")
assert_equals(format_duration(120), "2 minutes")
assert_equals(format_duration(3600), "1 hour")
assert_equals(format_duration(3662), "1 hour, 1 minute and 2 seconds")
assert_equals(format_duration(132030240), '4 years, 68 days, 3 hours and 4 minutes')