from microbit import*
import random

poss=("feuille","caillou","ciseau")

display.scroll(random.choice(poss))

while True:
    if button_a.is_pressed():
        display.scroll("WIN")
        sleep(1000)
        display.scroll(random.choice(poss))
    elif button_b.is_pressed():
        display.scroll("LOSE")
        sleep(1000)
        display.scroll(random.choice(poss))