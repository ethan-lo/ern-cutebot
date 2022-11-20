def on_received_number(receivedNumber):
    global v
    v = receivedNumber
radio.on_received_number(on_received_number)

def on_received_string(receivedString):
    global angle_next, v
    if receivedString == "heart":
        basic.show_leds("""
            . # . # .
                        . # . # .
                        . # . # .
                        . # . # .
                        . . # . .
        """)
        cuteBot.color_light(cuteBot.RGBLights.RGB_R, 0xffff00)
        cuteBot.color_light(cuteBot.RGBLights.RGB_L, 0xff0080)
        angle_next = angle_next + 10
        cuteBot.set_servo(cuteBot.ServoList.S1, angle_next)
        cuteBot.color_light(cuteBot.RGBLights.RGB_R, 0x0000ff)
        cuteBot.color_light(cuteBot.RGBLights.RGB_L, 0x0000ff)
        v = 0
    if receivedString == "smile":
        basic.show_leds("""
            . . . . .
                        . # . # .
                        . . . . .
                        # . . . #
                        . # # # .
        """)
        cuteBot.color_light(cuteBot.RGBLights.RGB_R, 0xff00ff)
        cuteBot.color_light(cuteBot.RGBLights.RGB_L, 0x0000ff)
    if receivedString == "diamond":
        basic.show_leds("""
            . . # . .
                        . . # . .
                        # # # # #
                        . . # . .
                        . . # . .
        """)
        cuteBot.color_light(cuteBot.RGBLights.RGB_R, 0xff8000)
        cuteBot.color_light(cuteBot.RGBLights.RGB_L, 0xff0000)
    if receivedString == "circle":
        basic.show_leds("""
            # . . . #
                        # . . . #
                        . # . # .
                        . # . # .
                        . . # . .
        """)
        cuteBot.color_light(cuteBot.RGBLights.RGB_R, 0xff9da5)
        cuteBot.color_light(cuteBot.RGBLights.RGB_L, 0xff0080)
        angle_next = 20
        cuteBot.set_servo(cuteBot.ServoList.S1, angle_next)
        cuteBot.color_light(cuteBot.RGBLights.RGB_R, 0xffff00)
        cuteBot.color_light(cuteBot.RGBLights.RGB_L, 0xffff00)
        v = 0
radio.on_received_string(on_received_string)

def on_received_value(name, value):
    global xValue, yValue
    if name == "x":
        xValue = value
    if name == "y":
        yValue = value
radio.on_received_value(on_received_value)

yValue = 0
xValue = 0
v = 0
angle_current = 0
angle_next = 0
music.play_melody("A G A F A G B C5 ", 400)
radio.set_group(20)
angle_next = 20
cuteBot.set_servo(cuteBot.ServoList.S1, angle_current)
cuteBot.color_light(cuteBot.RGBLights.RGB_L, 0xffff00)
cuteBot.color_light(cuteBot.RGBLights.RGB_R, 0xffff00)

def on_forever():
    global v
    cuteBot.motors(yValue + xValue, yValue - xValue)
    if v == 5:
        music.play_sound_effect(music.builtin_sound_effect(soundExpression.giggle),
            SoundExpressionPlayMode.UNTIL_DONE)
        v = 0
basic.forever(on_forever)
