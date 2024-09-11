###########################################################################################################################
####################################################     LIBRARIES     ####################################################
###########################################################################################################################

# Set the cwd to the one of the file
import os
if __name__ == '__main__':
    try: os.chdir(os.path.dirname(__file__))
    except: pass

from nxbt import Buttons, Sticks
from time import sleep

import sys; sys.path.append('..')
import Constants as CONST

# Used to toggle the direction when walking on the wild grass 
walking_direction = bool(0)

###########################################################################################################################
#################################################     INITIALIZATIONS     #################################################
###########################################################################################################################

# Go from "Change Grip/Order Menu" to the main menu and then go back to "Change Grip/Order Menu"
def test_macro(controller):
    controller.current_event = "Test"
    start_macro(controller)
    sleep(2); controller.current_button_pressed = 'HOME'
    controller.nxbt_manager.press_buttons(controller.controller_index, [Buttons.HOME])
    sleep(1); stop_macro(controller)

###########################################################################################################################

# Go from "Change Grip/Order Menu" to the main menu
def start_macro(controller):
    if controller.previous_event == controller.current_event: return
    
    controller.current_button_pressed = 'B'; sleep(1)
    controller.nxbt_manager.press_buttons(controller.controller_index, [Buttons.B])
    sleep(1); controller.current_button_pressed = 'HOME'
    controller.nxbt_manager.press_buttons(controller.controller_index, [Buttons.HOME])

###########################################################################################################################

# Go from "Change Grip/Order Menu" to the main menu and start the game
def fast_start_macro(controller):
    if controller.previous_event == controller.current_event: return
    
    controller.current_button_pressed = 'B'; sleep(1)
    controller.nxbt_manager.press_buttons(controller.controller_index, [Buttons.B])
    sleep(1); controller.current_button_pressed = 'HOME'
    controller.nxbt_manager.press_buttons(controller.controller_index, [Buttons.HOME])
    sleep(2); controller.current_button_pressed = 'A'
    controller.nxbt_manager.press_buttons(controller.controller_index, [Buttons.A])

###########################################################################################################################

# Pause the game and go to the "Change Grip/Order Menu"
def stop_macro(controller):
    if controller.previous_event == controller.current_event: return

    controller.current_button_pressed = 'HOME'
    controller.nxbt_manager.press_buttons(controller.controller_index, [Buttons.HOME])
    sleep(1.5); controller.current_button_pressed = 'DOWN'
    for _ in range(2): controller.nxbt_manager.press_buttons(controller.controller_index, [Buttons.DPAD_DOWN])
    for _ in range(4): 
        controller.current_button_pressed = 'RIGHT'; sleep(0.1) 
        controller.nxbt_manager.press_buttons(controller.controller_index, [Buttons.DPAD_RIGHT])
        controller.current_button_pressed = ''; sleep(0.1)
    sleep(0.5); controller.current_button_pressed = 'A'
    controller.nxbt_manager.press_buttons(controller.controller_index, [Buttons.A])
    sleep(2); controller.nxbt_manager.press_buttons(controller.controller_index, [Buttons.A]); sleep(1)
    controller.current_button_pressed = ''

###########################################################################################################################

# Fully restart the game (Hard reset)
def restart_game_macro(controller):
    if controller.previous_event == controller.current_event: return
    
    controller.current_button_pressed = 'HOME'
    controller.nxbt_manager.press_buttons(controller.controller_index, [Buttons.HOME])
    sleep(1.5); controller.current_button_pressed = 'X'
    controller.nxbt_manager.press_buttons(controller.controller_index, [Buttons.X]); sleep(0.5)
    if CONST.SKIP_UPDATING_GAME:
        sleep(0.5)
        for _ in range(2):
            controller.current_button_pressed = 'A'; sleep(0.2)
            controller.nxbt_manager.press_buttons(controller.controller_index, [Buttons.A])
            controller.current_button_pressed = ''
            sleep(0.8)
        for _ in range(3):
            controller.current_button_pressed = 'UP'; sleep(0.1)
            controller.nxbt_manager.press_buttons(controller.controller_index, [Buttons.DPAD_UP])
            controller.current_button_pressed = ''
    for _ in range(10):
        controller.current_button_pressed = 'A'; sleep(0.2)
        controller.nxbt_manager.press_buttons(controller.controller_index, [Buttons.A])
        controller.current_button_pressed = ''; sleep(0.1)

###########################################################################################################################

# The player moves Up/Down or Right/Left
def move_player_wild_macro(controller, direction = CONST.WILD_WALKING_DIRECTION, walking_duration = CONST.WILD_WALKING_SECONDS):
    global walking_direction

    if direction == 'NS':
        if not walking_direction:
            controller.current_button_pressed = 'UP'
            controller.nxbt_manager.press_buttons(
                controller.controller_index, [Buttons.DPAD_UP, Buttons.B], down=walking_duration)
        else: 
            controller.current_button_pressed = 'DOWN'
            controller.nxbt_manager.press_buttons(
                controller.controller_index, [Buttons.DPAD_DOWN, Buttons.B], down=walking_duration)

    elif direction == 'EW':
        if not walking_direction:
            controller.current_button_pressed = 'LEFT'
            controller.nxbt_manager.press_buttons(
                controller.controller_index, [Buttons.DPAD_LEFT, Buttons.B], down=walking_duration)
        else: 
            controller.current_button_pressed = 'RIGHT'
            controller.nxbt_manager.press_buttons(
                controller.controller_index, [Buttons.DPAD_RIGHT, Buttons.B], down=walking_duration)
    else:
        raise ValueError("Invalid direction. Use 'NS' for Up/Down or 'EW' for Right/Left")

    walking_direction = not walking_direction


def move_player_shaimin_macro(controller):
    global walking_direction

    # We want to go down
    walking_direction = True

    # Move down
    move_player_wild_macro(controller, 'NS', 5)

    # Go back to the top
    move_player_wild_macro(controller, 'NS', 5)

    # Start fight
    controller.current_button_pressed = 'A'; sleep(0.2)
    controller.nxbt_manager.press_buttons(controller.controller_index, [Buttons.A])
    controller.current_button_pressed = ''; sleep(0.1)

###########################################################################################################################

# Escape from the combat
def escape_combat_macro(controller):
    if controller.previous_event != controller.current_event: 
        controller.current_button_pressed = 'UP'
        controller.nxbt_manager.press_buttons(controller.controller_index, [Buttons.DPAD_UP])
    else:
        controller.current_button_pressed = 'A'
        controller.nxbt_manager.press_buttons(controller.controller_index, [Buttons.A]); sleep(0.1)
    
###########################################################################################################################

# Go to home menu
def home_macro(controller):
    controller.current_button_pressed = 'HOME'
    controller.nxbt_manager.press_buttons(controller.controller_index, [Buttons.HOME]); sleep(1)

###########################################################################################################################

# Selects the desired starter pokémon
def select_starter_macro(controller):
    if controller.previous_event == controller.current_event: return

    wait_and_press_single_button(controller, 1, 'A'); sleep(1)
    if CONST.STARTER == 'C': 
        controller.current_button_pressed = 'RIGHT'
        controller.nxbt_manager.press_buttons(controller.controller_index, [Buttons.DPAD_RIGHT]); sleep(0.2)
    elif CONST.STARTER == 'R': 
        controller.current_button_pressed = 'LEFT'
        controller.nxbt_manager.press_buttons(controller.controller_index, [Buttons.DPAD_LEFT]); sleep(0.2)
    controller.nxbt_manager.press_buttons(controller.controller_index, [Buttons.A])

###########################################################################################################################

# Selects the desired starter pokémon
def accept_selection_box_macro(controller):
    if controller.previous_event == controller.current_event: return

    controller.current_button_pressed = 'UP'
    for _ in range(2): controller.nxbt_manager.press_buttons(controller.controller_index, [Buttons.DPAD_UP])
    for _ in range(2): 
        controller.current_button_pressed = 'A'; sleep(0.2)
        controller.nxbt_manager.press_buttons(controller.controller_index, [Buttons.A])
        controller.current_button_pressed = ''; sleep(0.1)

###########################################################################################################################

# Enter the lake
def enter_lake_macro(controller):
    controller.current_button_pressed = 'UP'
    controller.nxbt_manager.press_buttons(controller.controller_index, [Buttons.DPAD_UP], down=0.5)
    controller.current_button_pressed = 'A'; sleep(0.2)
    controller.nxbt_manager.press_buttons(controller.controller_index, [Buttons.A])
    controller.current_button_pressed = ''; sleep(0.1)

###########################################################################################################################

def enter_static_combat_macro(controller):
    if CONST.MOVE_FORWARD_STATIC_ENCOUNTER:
        controller.current_button_pressed = 'UP'
        controller.nxbt_manager.press_buttons(controller.controller_index, [Buttons.DPAD_UP], down=0.5)
    press_single_button(controller, 'A')

###########################################################################################################################

# Press the specified button a single time
def press_single_button(controller, button):
    controller.current_button_pressed = button
    controller.nxbt_manager.press_buttons(controller.controller_index, [getattr(Buttons, button)])

###########################################################################################################################

# Wait the specified time and press the button a single time
def wait_and_press_single_button(controller, seconds, button):
    sleep(seconds)
    press_single_button(controller, button)

###########################################################################################################################
#####################################################     PROGRAM     #####################################################
###########################################################################################################################

