def wind_chill(temperature, wind_speed):
    if wind_speed < 3 or temperature > 50:
        return None
    wind_chill = 35.74 + 0.6215 * temperature - 35.75 * wind_speed ** 0.16 + 0.4275 * temperature * wind_speed ** 0.16
    return wind_chill

def celsius_to_fahrenheit(celsius_temp):
    return celsius_temp * 9/5 + 32

temperature = float(input("What is the temperature? "))
temp_unit = input("Fahrenheit or Celsius (F/C)? ").upper()

if temp_unit == 'C':
    temperature = celsius_to_fahrenheit(temperature)

for wind_speed in range(5, 61, 5):
    wind_chill_val = wind_chill(temperature, wind_speed)
    if wind_chill_val is not None:
        print(f"At temperature {temperature:.2f}F, and wind speed {wind_speed} mph, the windchill is {wind_chill_val:.2f}.")
        if temperature < 50 and wind_chill_val < 40:
            print("You should wear warm clothing and cover exposed skin to avoid frostbite.")
        else:
            print("You do not need to wear extra layers.")
    else:
        print(f"At temperature {temperature:.2f}F, and wind speed {wind_speed} mph, the windchill is undefined.")
