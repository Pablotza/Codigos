def calculate_wind_chill(temp, wind_speed):
    if temp < 50 and wind_speed > 3:
        wind_chill = 35.74 + (0.6215 * temp) - (35.75 * (wind_speed ** 0.16)) + (0.4275 * temp * (wind_speed ** 0.16))
        return wind_chill
    else:
        return temp

def convert_to_fahrenheit(temp_celsius):
    temp_fahrenheit = (temp_celsius * 9/5) + 32
    return temp_fahrenheit

#Extra
def recommend_dressing(temp, wind_speed):
    wind_chill = calculate_wind_chill(temp, wind_speed)
    if temp >= 80:
        print("Recommendation: wear cool and light clothing.")
    elif temp >= 60:
        if wind_chill < 60:
            print("Recommendation: wear a light jacket.")
        else:
            print("Recommendation: wear a warmer jacket.")
    elif temp >= 40:
        if wind_chill < 50:
            print("Recommendation: wear a warm jacket.")
        else:
            print("Recommendation: wear a winter jacket.")
    else:
        print("Recommendation: wear winter clothing, scarf, hat, and gloves.")

temp_input = input("What is the temperature? ")
temp_scale = input("Fahrenheit or Celsius (F/C)? ")

if temp_scale.upper() == "F":
    temp = float(temp_input)
else:
    temp = convert_to_fahrenheit(float(temp_input))

print(f"At temperature {temp:.1f}{temp_scale}, and wind speed 5 mph, the windchill is: {calculate_wind_chill(temp, 5):.2f}{temp_scale}")
for speed in range(10, 65, 5):
    print(f"At temperature {temp:.1f}{temp_scale}, and wind speed {speed} mph, the windchill is: {calculate_wind_chill(temp, speed):.2f}{temp_scale}")

recommend_dressing(temp, 5)
