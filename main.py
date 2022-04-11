def Restart():
    global PlayerHP, Food, Hunger
    basic.show_string("......Done")
    PlayerHP = 10
    Food = 0
    Hunger = 15

def on_button_pressed_ab():
    basic.show_string("HP")
    basic.show_number(PlayerHP)
    basic.show_string("Hunger")
    basic.show_number(Hunger)
    basic.show_string("Food")
    basic.show_number(Food)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

Ran = 0
Ran_2 = 0
Hunger = 0
Food = 0
PlayerHP = 0
PlayerHP = 10
Food = 0
Hunger = 15

def on_forever():
    pass
basic.forever(on_forever)

def on_forever2():
    pass
basic.forever(on_forever2)

def on_forever3():
    global Ran_2, Food, Hunger, Ran
    Ran_2 = randint(-10, 10)
    if Ran_2 == 9:
        basic.show_leds("""
            # # . . .
                        # # . . .
                        # # # # #
                        . # # # .
                        . # . # .
        """)
        basic.pause(500)
        if input.button_is_pressed(Button.A):
            basic.show_string("You kill him")
            basic.show_string("+1 food")
            Food += 1
            basic.pause(2000)
        elif input.button_is_pressed(Button.B):
            basic.show_string("ok")
        basic.clear_screen()
        Ran_2 += 1
    basic.pause(100)
    if randint(0, 10) == 3:
        basic.show_string("-1 Hunger")
        basic.show_string("eat?")
        if input.button_is_pressed(Button.A):
            Food += -1
            Hunger += 1
        elif input.button_is_pressed(Button.B):
            basic.show_string("ok")
            Hunger += -1
            Ran += 1
basic.forever(on_forever3)

def on_in_background():
    if True:
        if Hunger == -1:
            basic.show_string("YOU DIE")
            basic.pause(500)
            basic.show_string("Press B to restart")
            basic.clear_screen()
            basic.pause(100000000)
            Restart()
control.in_background(on_in_background)
