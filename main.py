def on_button_pressed_a():
    global count
    count += 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    basic.show_string("see you")
    control.reset()
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_button_pressed_ab():
    global count
    count = 0
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global count
    if count > 0:
        count += 0 - 1
input.on_button_pressed(Button.B, on_button_pressed_b)

count = 0
basic.show_string("hello")

def on_forever():
    basic.show_number(count)
basic.forever(on_forever)
