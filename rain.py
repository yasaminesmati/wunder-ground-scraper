"""
enum class for conditions value
"""
import enum
import pandas as pd
import string
#print(wu_cond)
class Conditions(enum.Enum):
    LIGHT_RAIN = "light rain"
    RAIN="rain"
    HEAVY_RAIN="heavy rain"
    LIGHT_SNOW="light snow"
    SNOW="snow"
    HEAVY_SNOW="heavy snow"
    PARTLY_CLOUDY="partly cloudy"
    MOSTLY_CLOUDY="mostly cloudy"
    CLOUDY="cloudy"
    FAIR="fair"
    SAND="sand"
    WINDY="windy"
    FOGGY="foggy"

class States:
    def assignState(self, wu_cond: str):
        wu_cond = wu_cond.lower()

        char_to_replace = {'/': ' ',
                   '-': ' ',}

        for key, value in char_to_replace.items():
            wu_cond = wu_cond.replace(key, value)

        if wu_cond.find("heavy snow") >=0:
            return Conditions.HEAVY_SNOW.value
        
        if wu_cond.find("light snow") >=0:
            return Conditions.LIGHT_SNOW.value

        if wu_cond.find("hail") >=0:
            return Conditions.LIGHT_SNOW.value 

        if wu_cond.find("wintry mix") >=0:
            return Conditions.LIGHT_SNOW.value

        if wu_cond.find("heavy rain") >=0:
            return Conditions.HEAVY_RAIN.value

        if wu_cond.find("snow") >=0:
            return Conditions.SNOW.value    

        if wu_cond.find("t storm") >=0:
            return Conditions.RAIN.value
        
        if wu_cond.find("thunder") >=0:
            return Conditions.RAIN.value

        if wu_cond.find("light rain") >=0:
            return Conditions.LIGHT_RAIN.value

        if wu_cond.find("light drizzle") >=0:
            return Conditions.LIGHT_RAIN.value

        if wu_cond.find("drizzle") >=0:
            return Conditions.RAIN.value

        if wu_cond.find("rain") >=0:
            return Conditions.RAIN.value

        if wu_cond.find("mostly cloudy") >=0:
            return Conditions.MOSTLY_CLOUDY.value

        if wu_cond.find("partly cloudy") >=0:
            return Conditions.PARTLY_CLOUDY.value
        
        if wu_cond.find("widespread dust") >=0:
            return Conditions.LIGHT_RAIN.value    
        
        if wu_cond.find("cloudy") >=0:
            return Conditions.CLOUDY.value  

        if wu_cond.find("windy") >=0:
            return Conditions.WINDY.value  

        if wu_cond.find("sand") >=0:
            return Conditions.SAND.value

        if wu_cond.find("fog") >=0:
            return Conditions.FOGGY.value
        
        if wu_cond.find("haze") >=0:
            return Conditions.FOGGY.value

        if wu_cond.find("mist") >=0:
            return Conditions.FOGGY.value
        
        if wu_cond.find("fair") >=0:
            return Conditions.FAIR.value

        else:
            print(string(wu_cond))





