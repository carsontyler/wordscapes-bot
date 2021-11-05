from pynput.mouse import Button, Controller
import time


def input_word(word, input_characters, bbox):
    mouse = Controller()
    word_character_list = list(word)

    bx, by = bbox

    for character in word_character_list:
        character_position = input_characters[character]
        x = bx + (character_position['x'] + (character_position['w'] / 2))
        y = by + (character_position['y'] + (character_position['h'] / 2))

        # mouse.position = (x, y)
        # mouse.press(Button.left)
        # print(f'Moved mouse to {mouse.position}')

        time.sleep(1)

    mouse.release(Button.left)
