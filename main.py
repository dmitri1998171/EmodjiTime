'''
TODO

+ 1) get a time
+ 2) parse a time
3) collect emodji
4) show the emodji

'''

import datetime

now = str(datetime.datetime.now().time())       # get a time in str
now = now.split('.')                            # delete millis
time = now[0]
print(time)

time = time.split(":")                          
time.pop()                                      # delete seconds
print(time)


