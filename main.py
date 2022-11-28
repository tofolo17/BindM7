import time

import keyboard
import pydirectinput

# Hotkeys
ATTRIBUTE = "ctrl+."
UNBID = "ctrl+;"
BREAK = "ctrl+enter"

# Constants
ATTRIBUTIONS = {
    'q': '',
    'w': '',
    'e': '',
    'r': '',
    'space': ''
}
OPTIONS = ['e', 'm']
TIMER = 10


# Loop principal
def main():
    while True:
        if keyboard.is_pressed(ATTRIBUTE):
            atribuir()
        if keyboard.is_pressed(UNBID):
            desvincular()
        if keyboard.is_pressed(BREAK):
            break
        for key, value in ATTRIBUTIONS.items():
            if keyboard.is_pressed(key):
                if value == 'e':
                    pydirectinput.press('t')
                else:
                    pydirectinput.keyDown('ctrl')
                    pydirectinput.press('6')
                    pydirectinput.keyUp('ctrl')


# Atribuição
def atribuir():
    print("#" * 5, "Atribuição", "#" * 5)
    c = recebe_comando()
    print(f"Comando: {c}")
    time.sleep(0.5)

    r = None
    if c:
        print("Comando recebido!")
        r = recebe_resposta()
        print(f"Resposta: {r}")
    if r:
        ATTRIBUTIONS[c] = r
        print(f"Atualizações:\n{ATTRIBUTIONS}")
    print("Saindo de atribuir()")


def recebe_algo(options):
    ini = time.time()
    while time.time() - ini < TIMER:
        for key in options:
            if keyboard.is_pressed("ctrl+" + key):
                return key


def recebe_comando():
    return recebe_algo(ATTRIBUTIONS)


def recebe_resposta():
    return recebe_algo(OPTIONS)


# Desvínculo
def desvincular():
    print("#" * 5, "Desvínculo", "#" * 5)
    c = recebe_comando()
    print(f"Comando: {c}")
    if c is not None:
        if c == 'space':
            for key in ATTRIBUTIONS:
                ATTRIBUTIONS[key] = ''
        else:
            ATTRIBUTIONS[c] = ''
        print(f"Atualizações:\n{ATTRIBUTIONS}")
    print("Saindo de desvincular()")


main()
