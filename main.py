np = neopixel.create(DigitalPin.P1, 2, NeoPixelMode.RGB)

def on_forever():
    basic.show_icon(IconNames.HEART)
    np.clear()
    np.set_pixel_color(0, neopixel.colors(neopixel.rgb(15, 15, 0)))
    np.set_pixel_color(1, neopixel.colors(neopixel.rgb(15, 15, 15)))
    np.show()
    basic.show_icon(IconNames.YES)
basic.forever(on_forever)
