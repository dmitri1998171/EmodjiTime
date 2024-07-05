'''
TODO

+ 1) get a time
+ 2) parse a time
+ 3) collect emodji
+ 4) show the emodji

'''

import time

emodjies = {
    "12:00" : "\U0001F55B",
    "12:30" : "\U0001F567",
    "1:00" : "\U0001F550",
    "1:30" : "\U0001F55C",
    "2:00" : "\U0001F551",
    "2:30" : "\U0001F55D",
    "3:00" : "\U0001F552",
    "3:30" : "\U0001F55E",
    "4:00" : "\U0001F553",
    "4:30" : "\U0001F55F",
    "5:00" : "\U0001F554",
    "5:30" : "\U0001F560",
    "6:00" : "\U0001F555",
    "6:30" : "\U0001F561",
    "7:00" : "\U0001F556",
    "7:30" : "\U0001F562",
    "8:00" : "\U0001F557",
    "8:30" : "\U0001F563",
    "9:00" : "\U0001F558",
    "9:30" : "\U0001F564",
    "10:00" : "\U0001F559",
    "10:30" : "\U0001F565",
    "11:00" : "\U0001F55A",
    "11:30" : "\U0001F566"
}

# Getting a time
hours = time.localtime().tm_hour
minutes = time.localtime().tm_min

# Convert 24 to 12
if(hours > 12):
    hours -= 12

# Parsing
if(minutes < 15):                               # 00 - 15
    minutes = '00'

elif(minutes > 15 and minutes < 30):            # 15 - 30
    minutes = '30'
    
elif(minutes > 30 and minutes < 45):            # 30 - 45
    minutes = '30'

elif(minutes > 45):                             # 45 - 00
    minutes = '00'

    if(hours == 12):
        hours = 0
    else:
        hours += 1

hours = str(hours)

# Print time
selector = f"{hours}:{minutes}"
print(selector)

# Print emodji
print(emodjies[selector])