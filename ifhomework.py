"""
Create a function that accepts 3 parameters and checks for equality between any two of them.

Your function should return True if 2 or more of the parameters are equal, and false is none of them are equal to any of the others.
"""


inBathroom = False
inBath = False
Water = "Off"
Light = "Off"
WaterTemp = 14

if inBathroom == True and inBath == True and Water == "On" and WaterTemp <= 30 :
    WaterTemp += 6
    Light = "On"
    Water = "On"

elif inBathroom == True and inBath == False and Water == "On" and WaterTemp > 43:
    Light = "On"
    Water = "Off"
    WaterTemp = WaterTemp - 3

else:
    WaterTemp = 29
    Water = "Off"
    Light = "Off"

print(WaterTemp)
print(Light)
print(Water)


