let tempf = 60
while (true) {
    console.log("temperature" + input.temperature(TemperatureUnit.Fahrenheit))
    if (input.temperature(TemperatureUnit.Fahrenheit) > tempf) {
        light.setPixelColor(5, light.rgb(255, 0, 0))
    } else {
        light.clear()
    }
    
}
// if tempF > 60:
// light.set_pixel_color(5, light.rbg(0, 255, 0))
if (tempf > 1000) {
    light.setPixelColor(5, light.rgb(255, 0, 0))
} else if (tempf > 40) {
    light.setPixelColor(5, light.rgb(0, 255, 0))
} else {
    light.setPixelColor(5, light.rgb(0, 0, 255))
}

