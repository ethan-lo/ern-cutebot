radio.onReceivedString(function (receivedString) {
    if (receivedString == "heart") {
        basic.showLeds(`
            . # . # .
            . # . # .
            . # . # .
            . # . # .
            . . # . .
            `)
        cuteBot.colorLight(cuteBot.RGBLights.RGB_R, 0xffff00)
        cuteBot.colorLight(cuteBot.RGBLights.RGB_L, 0xff0080)
        angle_next = angle_next + 10
        cuteBot.setServo(cuteBot.ServoList.S1, angle_next)
        cuteBot.colorLight(cuteBot.RGBLights.RGB_R, 0x0000ff)
        cuteBot.colorLight(cuteBot.RGBLights.RGB_L, 0x0000ff)
        v = 0
    }
    if (receivedString == "smile") {
        basic.showLeds(`
            . . . . .
            . # . # .
            . . . . .
            # . . . #
            . # # # .
            `)
        cuteBot.colorLight(cuteBot.RGBLights.RGB_R, 0xff00ff)
        cuteBot.colorLight(cuteBot.RGBLights.RGB_L, 0x0000ff)
    }
    if (receivedString == "diamond") {
        basic.showLeds(`
            . . # . .
            . . # . .
            # # # # #
            . . # . .
            . . # . .
            `)
        cuteBot.colorLight(cuteBot.RGBLights.RGB_R, 0xff8000)
        cuteBot.colorLight(cuteBot.RGBLights.RGB_L, 0xff0000)
    }
    if (receivedString == "circle") {
        basic.showLeds(`
            # . . . #
            # . . . #
            . # . # .
            . # . # .
            . . # . .
            `)
        cuteBot.colorLight(cuteBot.RGBLights.RGB_R, 0xff9da5)
        cuteBot.colorLight(cuteBot.RGBLights.RGB_L, 0xff0080)
        angle_next = 20
        cuteBot.setServo(cuteBot.ServoList.S1, angle_next)
        cuteBot.colorLight(cuteBot.RGBLights.RGB_R, 0xffff00)
        cuteBot.colorLight(cuteBot.RGBLights.RGB_L, 0xffff00)
        v = 0
    }
})
radio.onReceivedValue(function (name, value) {
    if (name == "x") {
        xValue = value
    }
    if (name == "y") {
        yValue = value
    }
    cuteBot.motors(yValue + xValue, yValue - xValue)
})
let yValue = 0
let xValue = 0
let v = 0
let angle_current = 0
let angle_next = 0
music.playMelody("A G A F A G B C5 ", 400)
radio.setGroup(20)
angle_next = 20
cuteBot.setServo(cuteBot.ServoList.S1, angle_current)
cuteBot.colorLight(cuteBot.RGBLights.RGB_L, 0xffff00)
cuteBot.colorLight(cuteBot.RGBLights.RGB_R, 0xffff00)
