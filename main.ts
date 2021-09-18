let np = neopixel.create(DigitalPin.P1, 2, NeoPixelMode.RGB)
basic.forever(function on_forever() {
    basic.showIcon(IconNames.Heart)
    np.clear()
    np.setPixelColor(0, neopixel.colors(neopixel.rgb(15, 15, 0)))
    np.setPixelColor(1, neopixel.colors(neopixel.rgb(15, 15, 15)))
    np.show()
    basic.showIcon(IconNames.Yes)
})
