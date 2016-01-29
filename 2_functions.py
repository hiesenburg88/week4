import faa

# Change the following code all you want:
def get_city_for(data):
  return data['city']

def get_temperature_at(code):
  data = faa.get_weather(code)
  return data['weather']['temp']

def get_wind_at(code):
  data = faa.get_weather(code)
  return data['weather']['wind']


# Do not change the code below this line.

print("O'Hare Airport serves the city of", get_city_for(data))
print("The temperature is:", get_temperature_at('ORD'))
print("The wind is:", get_wind_at('ORD'))

print(sport)
