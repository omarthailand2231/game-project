function Restart () {
    basic.showString("......Done")
    PlayerHP = 10
    Food = 0
    Hunger = 15
}
input.onButtonPressed(Button.AB, function () {
    basic.showString("HP")
    basic.showNumber(PlayerHP)
    basic.showString("Hunger")
    basic.showNumber(Hunger)
    basic.showString("Food")
    basic.showNumber(Food)
})
let Ran_2 = 0
let Hunger = 0
let Food = 0
let PlayerHP = 0
PlayerHP = 10
Food = 0
Hunger = 15
basic.forever(function () {
    Ran_2 = randint(-10, 10)
    if (Ran_2 == 9) {
        basic.showLeds(`
            # # . . .
            # # . . .
            # # # # #
            . # # # .
            . # . # .
            `)
        basic.pause(500)
        if (input.buttonIsPressed(Button.A)) {
            basic.showString("You kill him")
            basic.showString("+1 food")
            Food += 1
            basic.pause(2000)
        } else if (input.buttonIsPressed(Button.B)) {
            basic.showString("ok")
        }
        basic.clearScreen()
        Ran_2 += 1
    }
    basic.pause(100)
})
control.inBackground(function () {
    if (Hunger == -1) {
        basic.showString("YOU DIE")
        basic.pause(500)
        basic.showString("Press B to restart")
        basic.clearScreen()
        basic.pause(100000000)
        Restart()
    }
})
