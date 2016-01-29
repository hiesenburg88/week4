# 1. Look at these websites first:
#
#    http://www.fly.faa.gov/flyfaa/usmap.jsp
#    http://services.faa.gov/docs/services/airport


# 2. Write code to report weather information at various airports.
#
#    I have provided a Python module in this folder named "faa"
#    that contains a function that you will find helpful.
#
#    Your goal is to write code that will display weather
#    information for each airport code in the list below.
#
#    Example output for an airport code:
#
#    ORD (Chicago): The temperature is 30.0 F (-1.1 C), and the wind is Northeast at 8.1mph.
#
#    Good luck!

airport_codes = ['ORD', 'SFO', 'JFK']
import faa

# Your code goes here:
for code in airport_codes:
    data = faa.get_weather(code)
    city = data['city']
    temp = data['weather']['temp']
    wind = data['weather']['wind']
    print(code, "(" + data['city'] +")", ": The temperature is", data['weather']['temp'], " and the wind is", data['weather']['wind'])
