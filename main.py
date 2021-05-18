import keyboard
import pydirectinput


def control_input(message: str, choices: list):
    print(message)
    while True:
        choice = input("Sua escolha: ").lower().strip()
        if choice in choices:
            break
        else:
            print("Inválido.")
    return choice


def trigger_input():
    t = control_input(
        message="\nTeclas de bind disponíveis:\nQ  ||  W  ||  E  ||  R",
        choices=['q', 'w', 'e', 'r']
    )
    a = control_input(
        message="\nMétodos de tilt:\nM - Maestria  ||  E - Emote", choices=["m", "e"]
    )

    return t, a


key_trigger, key_action = trigger_input()

while True:
    if keyboard.is_pressed(key_trigger):
        if key_action == "m":
            pydirectinput.keyDown('ctrl')
            pydirectinput.press('6')
            pydirectinput.keyUp('ctrl')
        else:
            pydirectinput.press('t')
    elif keyboard.is_pressed('-'):
        key_trigger, key_action = trigger_input()
