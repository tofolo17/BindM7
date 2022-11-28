import keyboard
import pydirectinput


def main():
    key_trigger, key_action = trigger_input()
    print(f'\nTudo pronto! Para reiniciar, aperte "-".\n')

    while True:
        if keyboard.is_pressed(key_trigger):
            if key_action == "m":
                pydirectinput.keyDown('ctrl')
                pydirectinput.press('6')
                pydirectinput.keyUp('ctrl')
            else:
                pydirectinput.press('t')
        elif keyboard.is_pressed('-'):
            main()


def trigger_input():
    print("Teclas de bind disponíveis:\nQ  ||  W  ||  E  ||  R")
    t = input(f'Sua escolha: ').upper()
    while t not in ['Q', 'W', 'E', 'R']:
        t = input(f'Sua escolha: ').upper()

    print("\nMétodos de tilt:\nM - Maestria  ||  E - Emote")
    a = input(f'Sua escolha: ').upper()
    while a not in ['M', 'E']:
        a = input(f'Sua escolha: ').upper()

    return t, a


main()
