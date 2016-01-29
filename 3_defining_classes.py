# Classifying things
# Classes vs. instances, data attributes, and methods.

import faa;

class Airport:
  pass

  def city()
    data = faa.get_weather(....)
    return data['city']



my_airport = Airport()
your_airport = Airport()
my_airport.code = 'ORD'

print("O'Hare Airport serves the city of", my_airport.city())
# print("The temperature is:", my_airport.temp())
# print("The wind is:", my_airport.wind())
