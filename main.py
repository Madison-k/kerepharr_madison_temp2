tempf = 60
while True:
    print("temperature"+ input.temperature(TemperatureUnit.FAHRENHEIT))
    if input.temperature(TemperatureUnit.FAHRENHEIT) > tempf:
        light.set_pixel_color(5, light.rgb(255, 0, 0))
    else :
         light.clear()

#if tempF > 60:
    #light.set_pixel_color(5, light.rbg(0, 255, 0))

if tempf >1000:
    light.set_pixel_color(5, light.rgb(255, 0, 0))
elif tempf > 40:
    light.set_pixel_color(5, light.rgb(0, 255, 0))
else:
    light.set_pixel_color(5, light.rgb (0, 0, 255))

#if tempF > 70:
    #light.set_all(light.rbg(255, 0, 0))
#elif tempF > 40:
    #light.set_all(lighrt.rbg(0, 255, 0)) 
#else:
    #light.set_all(light.rbg(0, 0, 255))       