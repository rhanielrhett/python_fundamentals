#!/bin/python3
import os
import sys

def convertTime(time):
    # Case AM and 12 something
    if time[-2:]=='AM' and time[:2]=='12':
        return '00' + time[2:8]

    # Case AM and later than 12, here we only cut AM
    elif time[-2:] == 'AM':
        return time[:-2]
    
    # Case PM and is 12
    elif time[-2:]=='PM' and time[:2]=='12':
        return time[:-2]

    # Add 12 hours to PM time when it's not 12
    else:
        return str(int(time[:2]) + 12) + time[2:8]    

if __name__ == '__main__':
    #f = open(os.environ['OUTPUT_PATH'], 'w')
    time = input('Enter the time in 12-hour format: ') # Example format 07:10:23PM, goes without ''
    result = convertTime(time)
    #f.write(result + '\n')
    #f.close()
    print('Time Conversion:', result)
