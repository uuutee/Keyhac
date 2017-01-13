import sys
import os

from keyhac import *


def configure(keymap):

    # --------------------------------------------------------------------
    # Text editer setting for editting config.py file

    # Setting with program file path (Simple usage)
    if 1:
        keymap.editor = "Sublime Text"

    # Setting with callable object (Advanced usage)
    if 0:
        def editor(path):
            subprocess.call([ "open", "-a", "Sublime Text", path ])
        keymap.editor = editor


    # --------------------------------------------------------------------
    # Customizing the display

    # Font
    keymap.setFont( "Osaka-Mono", 16 )

    # Theme
    keymap.setTheme("black")


    # --------------------------------------------------------------------

    # Global keymap which affects any windows
    keymap_global = keymap.defineWindowKeymap()

    # Moving active window by keyboard
    if 1:
        # Ctrl-Alt-Up/Down/Left/Right : Move active window by 10 pixel unit
        keymap_global[ "Ctrl-Alt-Left"  ] = keymap.MoveWindowCommand( -10, 0 )
        keymap_global[ "Ctrl-Alt-Right" ] = keymap.MoveWindowCommand( +10, 0 )
        keymap_global[ "Ctrl-Alt-Up"    ] = keymap.MoveWindowCommand( 0, -10 )
        keymap_global[ "Ctrl-Alt-Down"  ] = keymap.MoveWindowCommand( 0, +10 )

    if 1:
        # Cursor keys
        keymap_global[ "Ctrl-P" ] = "Up"    
        keymap_global[ "Ctrl-N" ] = "Down"  
        keymap_global[ "Ctrl-F" ] = "Right"  
        keymap_global[ "Ctrl-B" ] = "Left"  
        keymap_global[ "Ctrl-J" ] = "Enter" 
