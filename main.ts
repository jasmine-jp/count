input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    count += 1
})
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    basic.showString("see you")
    control.reset()
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    
    count = 0
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    if (count > 0) {
        count += 0 - 1
    }
    
})
let count = 0
basic.showString("hello")
basic.forever(function on_forever() {
    basic.showNumber(count)
})
